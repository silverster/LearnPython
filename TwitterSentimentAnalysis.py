import tweepy
from textblob import TextBlob

consumer_key = 'LZAACT1SMSCyBGKRQCDYOmQcP'
consumer_secret = 'xkUBqaJUKs3GngpAEak4NBkKfPUxP4qpIvNchO4zUb5MVHFeqK'

access_token = '305728345-itRUBro3xbXuFIZDH26szIhBTmKljcDgTHQAc7Ka'
accesstoken_secret = 'VfYmDDB8odtR56I8mgHrParyPqNkxltcxDhw0fFaMJexc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, accesstoken_secret)

api = tweepy.API(auth)

public_tweets = api.search('obama')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)