from Core import MongoDB
import json
from bson.objectid import ObjectId



def AuthLogin(email, password):
    
    filters = {"email":email,"password":password}
    project = {"_id":1}

    mongoList = MongoDB.Select("galata","users",filters,project)

    datax = json.loads(mongoList, encoding="utf-8")

    return datax