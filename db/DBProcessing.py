'''
Created on Jan 5, 2015

@author: nb
'''
from pymongo import MongoClient

dbclient = MongoClient("localhost",27017)
db = dbclient['mongodbdata']

data = {'name':'praveen'}
users = db.users
for user in users.find():
    print user