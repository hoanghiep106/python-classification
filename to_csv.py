from pymongo import MongoClient
import csv

client = MongoClient("mongodb://localhost:27017")

db = client.get_database('daily_tweets')

tweets = db.tweets.find()


with open('tweets.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for tweet in tweets:
        writer.writerow([tweet['text']])


