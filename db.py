from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client.get_database('daily_tweets')

tweets = db.tweets.find()
