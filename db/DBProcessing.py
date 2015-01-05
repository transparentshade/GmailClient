'''
Created on Jan 5, 2015

@author: nb
'''
from pymongo import MongoClient
from bson.json_util import json_lib
import json

dbclient = MongoClient("localhost",27017)
db = dbclient['mongodbdata']

data = {'name':'praveen'}
emails = db.emails

def insert_email(email_str):
    #emailObj = json.loads(email_str)
    emails.insert(email_str[0][1])
    print "Email inserted successfully ",email_str[0]['subject']