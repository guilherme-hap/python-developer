import tweepy
from secrets import CONSUMER_KEY
from secrets import CONSUMER_SECRET
from secrets import ACCESS_TOKEN
from secrets import ACCESS_TOKEN_SECRET

BRAZIL_WOE_ID = 23424768

auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
