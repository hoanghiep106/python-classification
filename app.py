from csv_loader import tweets
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

stemmer = PorterStemmer()


def check_base_word(base_word):
	if base_word and len(base_word) > 1 and base_word.isalpha():
		stemmed_word = stemmer.stem(base_word)
		if stemmed_word not in base_vector and stemmed_word not in stopwords.words('english'):
			return True
	return False


# Create base vector
base_vector = []
for tweet in tweets:
	if tweet['text']:
		words = tweet['text'].split()
		for word in words:
			if check_base_word(word):
				base_vector.append(stemmer.stem(word))

# Transform tweets into vectors
for tweet in tweets:
	if tweet['text']:
		words = list(set(tweet['text'].split()))
		stemmed_words = [stemmer.stem(word) for word in words if word and len(word) > 1 and word.isalpha()]
		tweet_vector = []
		for ele in base_vector:
			tweet_vector.append(1 if ele in stemmed_words else 0)
