import csv

categories = {
	'Transportation': {
		'value': 0,
		'subcategory': {
			'Means of transport': 0,
			'Transportation Infrastructure': 1,
			'Transportation Services': 2,
		}
	},
	'Accommodation': {
		'value': 1,
		'subcategory': {
			'First class accommodation': 3,
			'Second class accommodation': 4,
		}
	},
	'Attraction': {
		'value': 2,
		'subcategory': {
			'Culture & Tradition': 5,
			'Scenic': 6,
			'Exhibition entertainment': 7,
			'Live entertainment': 8,
			'Shopping': 9,
			'Adventure tours and activities': 10,
		}
	},
	'Service and Ancillary': {
		'value': 3,
		'subcategory': {
			'Information & Guiding': 11,
			'Catering Service': 12,
			'Facility': 13,
		}
	},
	'Tourism broker': {
		'value': 4,
		'subcategory': {
			'Tourism agent & operator': 14,
		}
	}
}

tweets = []

with open('tweets-category.csv', encoding="iso-8859-1") as tweet_file:
	reader = csv.DictReader(tweet_file)
	for row in reader:
		tweet = {
			'text': row['Tweet'],
			'subcategory': categories[row['Category']]['subcategory'][row['Subcategory']],
			'category': categories[row['Category']]['value']
		}
		tweets.append(tweet)


test_tweets = []

with open('test-tweets-category.csv', encoding="iso-8859-1") as test_tweet_file:
	reader = csv.DictReader(test_tweet_file)
	for row in reader:
		tweet = {
			'text': row['Tweet'],
			'subcategory': categories[row['Category']]['subcategory'][row['Subcategory']],
			'category': categories[row['Category']]['value']
		}
		test_tweets.append(tweet)
