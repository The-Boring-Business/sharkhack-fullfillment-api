from flask_restful import Resource
from config import Config
from flask import request
import tweepy
import time

def setup_api(access_token, access_token_secret):
    auth = tweepy.OAuthHandler(Config.TWITTER_CONSUMER_KEY, Config.TWITTER_SECRET)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
