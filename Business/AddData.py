from Core import MongoDB
import json
from bson.objectid import ObjectId
import datetime

def Site(siteId, name, siteUrl, favicon, sourceUrl, isActive, categoryNumber):    
    request = {'siteId': siteId, 'name': name,'siteUrl':siteUrl,'favicon':favicon,'sourceUrl':sourceUrl,'isActive':isActive,'categoryNumber':categoryNumber}  
    MongoDB.InsertOne("ulak","sites",request)

def Category(categoryNumber, name, color):  
    request = {'categoryNumber': categoryNumber, 'name': name,'color':color}
    MongoDB.InsertOne("ulak","categories",request)

def News(siteId, title, description, link, imageLink, pubTime, groupId, types, stem, categoryNumber, index):
    request = {'siteId': siteId, 'title': title,'description':description,'link':link,'imageLink':imageLink,'pubTime':pubTime,'groupId':groupId,'type':types,'stem':stem,'categoryNumber':categoryNumber,'index':index}
    MongoDB.InsertOne("ulak","news",request)

def ClusteredNews(index, groupId, link, siteId, title, description, imageLink, types, stem, categoryNumber, siteName, categoryName, favIcon, catColor):
    
    if description is None:
        description = ""

    req = {'index': index, 'siteId': siteId, 'title': title,'description':description,'link':link,'imageLink':imageLink,'groupId':groupId,'type':types,'stem':stem, 'categoryNumber':categoryNumber, 'siteName':siteName, 'categoryName': categoryName, 'favIcon':favIcon, 'catColor':catColor}
    
    selected = { "groupId": groupId}
    updateSet =  {"$addToSet":{"news": req}}
    response = MongoDB.Update("ulak","clustrednews",selected, updateSet)

    if response.modified_count == 0:
        request = {"groupId":groupId,
                "news":[{'index': index, "siteId": siteId, "title": title,"description":description,"link":link,"imageLink":imageLink,"groupId":groupId,"type":types,"stem":stem,"categoryNumber":categoryNumber,'siteName':siteName, 'categoryName': categoryName, 'favIcon':favIcon, 'catColor':catColor}]
                }     
        MongoDB.InsertOne("ulak","clustrednews",request)


            




