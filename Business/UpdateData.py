from Core import MongoDB
import json
from bson.objectid import ObjectId
from Business import GetData,AddData
import time

def News(siteId, title, description, link, imageLink, pubTime, groupId, types, stem, categoryNumber):

    selected = { "link": link}
    updateSet = {"$set": {'title': title,'description':description,'imageLink':imageLink,'pubTime':pubTime,'groupId':groupId,'type':types,'stem':stem,'categoryNumber':categoryNumber}}
    MongoDB.Update("ulak","news",selected, updateSet)

def ClustredNews(groupId, index, websites, categories):
    selectOne = GetData.NewsByIndex(index)

    siteName, favIcon = FindInWebSite(selectOne['siteId'], websites)
    categoryName, categoryColor = FindInCategory(selectOne['categoryNumber'], categories)

    title = selectOne['title']
    description = selectOne['description']
    imageLink = selectOne['imageLink']
    link = selectOne['link']
    siteId = selectOne['siteId']
    types = selectOne['type']
    categoryNumber = selectOne['categoryNumber']
    stem = selectOne['stem']

    AddData.ClusteredNews(index, groupId, link, siteId, title, description, imageLink, types, stem, categoryNumber,siteName, categoryName ,favIcon, categoryColor)


def NewsStem(stem, id):
    selected = { "_id": ObjectId(id)}
    updateSet = {"$set": {'stem':stem}}
    MongoDB.Update("ulak","news",selected, updateSet)

def DropNews():
    MongoDB.Drop("ulak","news")
    MongoDB.Drop("ulak","clustrednews")


def FindInWebSite(id, websiteList):
    siteName = ""
    favIcon = ""
    for item in websiteList:
        if item["siteId"] == id:
            siteName = item["name"]
            favIcon = item["favicon"]
    return siteName, favIcon

def FindInCategory(id, categoryList):
    categoryName = ""
    color = ""
    for item in categoryList:
        if item["categoryNumber"] == id:
            categoryName = item["name"]
            color = item["color"]
    return categoryName, color
