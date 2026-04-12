from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["binance"]
collection = db["trades"]

def save_to_db(data):
    collection.insert_one(data)