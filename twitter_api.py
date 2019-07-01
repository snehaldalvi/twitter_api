import tweepy

print("HOLA !!!!")
 # use your token and api keys here
CONSUMER_KEY='' 
CONSUMER_SECRET=' '
ACCESS_KEY=''
ACCESS_SECRET=''

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)

auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

print("hey!!!!! this is twitter API")

api.mentions_timeline()
api.home_timeline()
				# OR

#we can also create a function
""" 


import sys
sys.path.append('C:\Python\Scrpits\Twitter')
import tweepy
import private
import datetime,time


auth=tweepy.OAuthHandler(private.TWITTER_APP_KEY,private.TWITTER_APP_SECRET)
auth.seth_access_token(private.TWITTER_KEY,private.TWITTER_SECRET)
api=tweepy.API(auth)

def get_tweets(api,username):
	page=1
	depend=False
	while(True):
		tweets=api.user_timeline(username,page=page)

		for tweet in tweets:
			if(datetime.datetime.now() - tweet.created_at).days < 14:
				print(tweet.text.encode("utf-8"))
			else:
				depend=True
				return
		if not depend:
			page+1
			time.sleep(1000)
get_tweets(api,"Hello !!!")


"""



