import flask
from flask import request, jsonify
import json
import collections
import pandas as pd
import psycopg2
from BeautifulSoup import *
from DataEngine import clustering, BeautifulSoup
from WebService import api_string
import datetime
from readability import Document

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def default():
    return "Welcome"

@app.route('/collectnewsdata')
def collect():
    start_time = datetime.datetime.now()
    print(str(start_time))
    get_news_data()
    start2_time = datetime.datetime.now()
    print(str(start2_time))
    #cluster_news()
    finish_time = datetime.datetime.now()
    print(str(finish_time))
    return str((start2_time - start_time).total_seconds()) + " - " +  str((finish_time - start2_time).total_seconds())

@app.route('/api/v1/resources/sites', methods=['GET'])
def site_list_service():
    return site_list()

@app.route('/api/v1/resources/categories', methods=['GET'])
def category_list_service():
    return category_list()

@app.route('/api/v1/resources/news', methods=['GET'])
def news_list_service():
    return news_list()

@app.route('/api/v1/resources/news_detail', methods=['GET'])
def news_detail_service():
    return news_detail()

@app.route('/api/v1/resources/clean', methods=['GET'])
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

    app.run(host='localhost', port=8080, debug=True)
