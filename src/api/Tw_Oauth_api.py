from model.user import User
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from requests_oauthlib import OAuth1Session
from config import Config

TWITTER_REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
CONSUMER_KEY = Config.TWITTER_CONSUMER_KEY
CONSUMER_SECRET = Config.TWITTER_SECRET


class Twitter_Api(Resource):
    def get(self):
        request_token = OAuth1Session(
        client_key=CONSUMER_KEY, client_secret=CONSUMER_SECRET, callback_uri="http://127.0.0.1:5000/api/oauth/twitter/callback")
        data = request_token.get(TWITTER_REQUEST_TOKEN_URL)
        if data.status_code == 200:
            request_token = str.split(data.text, '&')
            oauth_token = str.split(request_token[0], '=')[1]
            oauth_callback_confirmed = str.split(request_token[2], '=')[1]
            return {
                "oauth_token": oauth_token,
                "oauth_callback_confirmed": oauth_callback_confirmed,
            }
        else:
            return {
                "oauth_token": None,
                "oauth_callback_confirmed": "false",
            }
