from pymongo import MongoClient
import os

### MongoDB Database
MONGO_USER = os.environ['MONGO_INITDB_ROOT_USERNAME']
MONGO_PASSWORD = os.environ['MONGO_INITDB_ROOT_PASSWORD']
MONGO_DB = os.environ['MONGO_DB']
MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = os.environ['MONGO_PORT']

client = MongoClient(MONGO_HOST, int(MONGO_PORT))
db = client[MONGO_DB]