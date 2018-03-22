from pymongo import MongoClient
from nltk.stem import PorterStemmer

client = MongoClient("mongodb://localhost:27017")

db = client.get_database('daily_tweets')

tweets = db.tweets.find()

base_vector = []

stemmer = PorterStemmer()

for tweet in tweets:
    if tweet['text']:
        words = tweet['text'].split()
        for word in words:
            if word and word.isalpha() and stemmer.stem(word) not in base_vector:
                base_vector.append(stemmer.stem(word))

tweets = db.tweets.find()

for tweet in tweets:
    if tweet['text']:
        words = list(set(tweet['text'].split()))
        stemmed_words = [stemmer.stem(word) for word in words if word.isalpha()]
        tweet_vector = []
        for ele in base_vector:
            tweet_vector.append(1 if ele in stemmed_words else 0)
        print(tweet_vector)
