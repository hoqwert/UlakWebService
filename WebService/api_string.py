import flask
from flask import request, jsonify
import json
import collections
from collections import OrderedDict
import pandas as pd
import psycopg2
from Business import AddData,GetData,UpdateData

def make_array(favicon):
    favicon_arr = favicon.split(',')
    return favicon_arr

def PubTimeShowString(date):
    duration = datetime.now() - date
    if duration.days == 0:
        duration_in_s = duration.total_seconds()
    else:
        duration_in_s = duration.total_seconds()
    return str(date)

def site_list():
    sites = GetData.MainSiteAdress()
    items = []
    for row in sites:
        s = collections.OrderedDict()
        s['id'] = row["_id"]["siteId"]
        s['name'] = row["_id"]["name"]
        s['image'] = row["_id"]["favicon"]
        items.append(s)
    return json.dumps(items)

def category_list():
    categories = GetData.Category()
    items = []
    for row in categories:
        s = collections.OrderedDict()
        s['id'] = row["categoryNumber"]
        s['name'] = row["name"]
        s['color'] = row["color"]
        items.append(s)
    return json.dumps(items)


def news_list():
    page = 0
    categoryId = 1

    data = GetData.ClustredNews(page,categoryId)
    items = []

    for newsGroup in data:
        s = collections.OrderedDict()
        s["GroupId"] = newsGroup["groupId"]
        s["NewsList"] = []
        s["Favicon"] = []
        for news in newsGroup["news"]:
            f = collections.OrderedDict()
            f['groupId'] = news["groupId"]
            f['favicon'] = news["favIcon"]
            f['title'] = news["title"]
            f['imageLink'] = news["imageLink"]
            f['newsid'] = news["index"]
            f['category'] = news["categoryName"]
            f['site'] = news["siteName"]
            f['color'] = news["catColor"]
            f['link'] = news["link"]
            s["NewsList"].append(f)
            s["Favicon"].append(news["favIcon"])
        items.append(s)
    return json.dumps(items)

def news_detail():
   # if 'id' in request.args:
   #     id = int(request.args['id'])
   #     groupId = int(request.args['groupId'])
   # else:
    #    return "Error: No id field provided. Please specify an id."
    groupId = 1
    data = GetData.ClustredNewsByGroupId(groupId)
    items = []

    for news in data[0]["news"]:
        d = collections.OrderedDict()
        d['newsid'] = ""
        d['groupId'] = news["groupId"]
        d['favicon'] = news["favIcon"]
        d['title'] = news["title"]
        d['imageLink'] = news["imageLink"]
        d['newsid'] = news["index"]
        d['category'] = news["categoryName"]
        d['site'] = news["siteName"]
        d['color'] = news["catColor"]
        d['link'] = news["link"]
        d['faviconList'] = make_array(news["favIcon"])

        items.append(d)
    return json.dumps(items)