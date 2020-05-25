from Core import MongoDB
import json
from bson.objectid import ObjectId



def Site():
    filters = {"isActive":1}
    project = {'siteId': 1, 'name': 1,'siteUrl':1,'favicon':1,'sourceUrl':1,'isActive':1,'categoryNumber':1}

    mongoList = MongoDB.Select("ulak","sites",filters,project)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax

def MainSiteAdress():
    filters = {"isActive":1}
    project = {'siteId','name','siteUrl','favicon','isActive'}

    mongoList = MongoDB.Distinct("ulak","sites",filters,project)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax

def Category():
    filters = {}
    project = {'categoryNumber': 1, 'name': 1,'color':1}

    mongoList = MongoDB.Select("ulak","categories",filters,project)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax

def SelectOneNewsByLink(link):
    
    filters = { "link" : link }
    project = {}
    mongoList = MongoDB.Select("ulak","news",filters,project)
    datax = json.loads(mongoList, encoding="utf-8")
    if datax.__len__() == 0:
        return 0
    else:
        return 1

def News():
    
    filters = {}
    project = {'siteId': 1, 'title': 1,'description':1,'link':1,'imageLink':1,'pubTime':1,'groupId':1,'type':1,'stem':1,'categoryNumber':1,'index':1}
    mongoList = MongoDB.Select("ulak","news",filters,project)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax

def NewsByIndex(index):
    
    filters = { "index" : index }
    project = {'siteId': 1, 'title': 1,'description':1,'link':1,'imageLink':1,'pubTime':1,'groupId':1,'type':1,'stem':1,'categoryNumber':1}
    mongoList = MongoDB.Select("ulak","news",filters,project)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax[0]

def ClustredNews(pageNo,categoryId):
    filters = {}
    project = {}
    mongoList = MongoDB.SelectByPage("ulak", "clustrednews",filters, project, pageNo, 10)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax

def ClustredNewsByGroupId(groupId):
    filters = {"groupId": groupId}
    project = {'news':1}
    mongoList = MongoDB.Select("ulak", "clustrednews",filters, project)
    datax = json.loads(mongoList, encoding="utf-8")
    return datax

