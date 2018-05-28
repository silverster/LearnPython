import tweepy
from textblob import TextBlob
import csv

consumer_key = 'LZAACT1SMSCyBGKRQCDYOmQcP'
consumer_secret = 'xkUBqaJUKs3GngpAEak4NBkKfPUxP4qpIvNchO4zUb5MVHFeqK'

access_token = '305728345-itRUBro3xbXuFIZDH26szIhBTmKljcDgTHQAc7Ka'
accesstoken_secret = 'VfYmDDB8odtR56I8mgHrParyPqNkxltcxDhw0fFaMJexc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, accesstoken_secret)

api = tweepy.API(auth)

public_tweets = api.search('oneplus6')


tweet_text = []
analysis_result = []
for tweet in public_tweets:
	#print(tweet.text)
	tweet_text.append(tweet.text)
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity>0.3 and analysis.sentiment.subjectivity<0.5:
		analysis_result.append('Fairly Positive')
	else: analysis_result.append('Negative or Neutral')

rows = zip(tweet_text,analysis_result)
with open('twitterexport.csv', 'w',encoding='utf-8') as myfile:
    writer = csv.writer(myfile)
    for row in rows:
        writer.writerow(row)
