
import json
import collections
import pandas as pd
import psycopg2
from DataEngine import clustering, BeautifulSoup
from WebServie import api_string
import datetime
from readability import Document

def site_list_service():
    return site_list()

def category_list_service():
    return category_list()

def news_list_service():
    return news_list()

def news_detail_service():
    return news_detail()

def cleanHtml():
    items = []
    url = ''
    article = ''
    articleBody = ''
    articleTitle = ''
    css = '<html><head><style type="text/css">p { font-family: Tahoma, Verdana; font-size: 38px;padding: 10px;10px;10px;10px; }</style></head>'

    if 'url' in request.args:
        url = request.args['url']
        response = requests.get(url)
        article = Document(response.text)
        articleTitle = article.title()
        articleBody = article.summary()
        #articleBody = articleBody.replace('<html>',css)

    items.append(articleTitle)
    items.append(articleBody)
    return json.dumps(items)

#news_list_service()
news_detail_service()