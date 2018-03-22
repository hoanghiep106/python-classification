import csv

tweets = []

with open('tweets-category.csv', encoding="iso-8859-1") as tweet_file:
	reader = csv.DictReader(tweet_file)
	for row in reader:
		tweet = {
			'text': row['Tweet'],
			'subcategory': row['Subcategory'],
		}
		tweets.append(tweet)