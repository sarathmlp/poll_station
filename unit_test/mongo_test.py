import sys
sys.path.append( '../')
from flask import Flask
import pymongo
from pymongo import MongoClient
import pprint
import ast
from models import Question
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017')
db = client.poll
poll_data = db.poll_data

cursor = poll_data.find().limit(1)
for data in cursor:
    pprint.pprint(data)
    last_id =  data['_id']

cursor = poll_data.find({'_id' : {'$gt' : ObjectId(last_id)}}). limit(1)
for data in cursor:
    pprint.pprint(data)
