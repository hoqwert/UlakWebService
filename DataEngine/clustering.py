# -*- coding: utf-8 -*-
import nltk
import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string
import json
from TurkishStemmer import TurkishStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.metrics.pairwise import cosine_similarity
import psycopg2
import pandas as pd
import numpy as np
import datetime
import sys
from Business import UpdateData,AddData,GetData
reload(sys)
sys.setdefaultencoding('utf-8')


def update_newsStem(stem, id):
    UpdateData.NewsStem(stem,id)

def select_newsAll():
    return GetData.News()

def select_newsStem():
    return GetData.News()


# Get default English stopwords and extend with punctuation
#stopwords = nltk.corpus.stopwords.words('english')
#stopwords.extend(string.punctuation)
#stopwords.append('')


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def get_stem(sentence):
    WPT = nltk.WordPunctTokenizer()
    stop_word_list = nltk.corpus.stopwords.words('turkish')
    #newStopWords = ['','']
    #stop_word_list.extend(newStopWords)
    stemmer = TurkishStemmer()
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenize(re.sub(r'\d+', '', sentence.strip()))]
    stems_a = [stemmer.stem(token) for token in tokens_a if token not in stop_word_list]
    return stems_a


def get_stems():
    newsAll = select_newsAll()

    for x in newsAll:
        stem = get_stem(x['title'].strip())
        update_newsStem(json.dumps(stem, ensure_ascii=False), x['_id']['$oid'])

    return select_newsStem()


def tokenize_and_stem(text):
    stemmer = TurkishStemmer()
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def clearData(text):
    returnText = text
    if "[CDATA[" in text:
        returnText = text.replace("<![CDATA[", "")
        returnText = returnText.replace("]]>", "")
    return returnText


def cluster_news():
    print('clustering 0 running...' + str(datetime.datetime.now()))
    threshold = 0.6
    newsSteam = get_stems()
    #newsAll = select_newsAll()
    sklearn_tfidf = TfidfVectorizer(norm='l2', min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)
    tfidf_matrix = sklearn_tfidf.fit_transform(t['stem'] for t in newsSteam)
 
    #terms = sklearn_tfidf.get_feature_names()
    print('clustering 1 running tfidf_matrix finished. >' + str(datetime.datetime.now()))
    result = cosine_similarity(tfidf_matrix)
    print("cluster 2 cosine_similarity finished. >" + str(datetime.datetime.now()))
    #data = pd.DataFrame(result).stack().reset_index()
    #data.columns = ['col1','col2','col3']

    group_id = 0
    temp_group_id = 0
    group_list = {}
    for w in newsSteam:
        group_list.setdefault(w['index'], [])

    for index1, i1 in enumerate(result):
        if not group_list[newsSteam[index1]['index']]:
            group_id = group_id + 1
            temp_group_id = group_id
            group_list[newsSteam[index1]['index']] = temp_group_id
        else:
            temp_group_id = group_list[newsSteam[index1]['index']]
        for index2, i2 in enumerate(i1):
            if i2 > threshold and i2 < 1:
                group_list[newsSteam[index2]['index']] = temp_group_id

    print("cluster 3 >" + str(datetime.datetime.now()))
    flipped = {}

    for key, value in group_list.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)

    print("cluster 4 >" + str(datetime.datetime.now()))
    websites = GetData.Site()
    categories = GetData.Category()

    for groupId in flipped:
        for index in flipped[groupId]:
            try:
                UpdateData.ClustredNews(groupId, index, websites, categories)
            except Exception as e:
                print(str(groupId) + " - " + str(index) + " > " + str(e))

    print("cluster 5 >" + str(datetime.datetime.now()))
    print('cluster 6 run.')