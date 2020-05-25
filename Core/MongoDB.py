#!/usr/bin/env python
#coding: utf8 
from pymongo import MongoClient
from bson.json_util import dumps


#client = MongoClient('35.226.130.8', username='ulak',password='ulak-2017', port=27017, authSource='admin',  authMechanism='SCRAM-SHA-1')
client = MongoClient("localhost", 27017, maxPoolSize=50)

def InsertOne(databaseName, collectionName, request):
    db = client[databaseName]
    collection = db[collectionName]
    response =  collection.insert_one(request)

def InsertMany(databaseName, collectionName, request):
    db = client[databaseName]
    collection = db[collectionName]
    collection.insert_many(request)

def Select(databaseName, collectionName, filters, projects):
    db = client[databaseName]
    collection = db[collectionName]
    return dumps(collection.find(filters, projects), ensure_ascii=False)

def Distinct(databaseName, collectionName, filters, projects):
    db = client[databaseName]
    collection = db[collectionName]
    return dumps(collection.aggregate([{"$group": {"_id":{"siteId":"$siteId", "name":"$name", "favicon":"$favicon"}}}]), 
    ensure_ascii=False)

def SelectOne(databaseName, collectionName, filters, projects):
    db = client[databaseName]
    collection = db[collectionName]
    return dumps(collection.find_one(filters, projects), ensure_ascii=False)
    
def Update(databaseName, collectionName, query, newValues):
    db = client[databaseName]
    collection = db[collectionName]
    collection.update
    return collection.update_one(query, newValues)

def Drop(databaseName, collectionName):
    db = client[databaseName]
    collection = db[collectionName]
    return collection.drop()

def SelectByPage(databaseName, collectionName, filters, projects, pageNo, limit):
    db = client[databaseName]
    collection = db[collectionName]
    result = collection.find().skip(pageNo * limit).limit(limit)
    return dumps(result,  ensure_ascii=False)



