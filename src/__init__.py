from flask_restful import Api
from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from src.routes.routes import initialize_routes
from config import Config
from flask_cors import CORS
from requests_oauthlib import OAuth1Session


# Place where app is defined
app = Flask(__name__)
app.config.from_object(Config)


TWITTER_REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
TWITTER_ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
CONSUMER_KEY = Config.TWITTER_CONSUMER_KEY
CONSUMER_SECRET = Config.TWITTER_SECRET
CALLBACk = Config.TWITTER_CALLBACK



@app.route("/request_token")
def request_oauth_token():
    request_token = OAuth1Session(
        client_key=CONSUMER_KEY, client_secret=CONSUMER_SECRET, callback_uri=CALLBACk
    )
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

@app.route("/access_token")
def request_access_token():
    oauth_token = OAuth1Session(
        client_key=CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=request.args.get("oauth_token"),
    )
    data = {"oauth_verifier": request.args.get("oauth_verifier")}
    response = oauth_token.post(TWITTER_ACCESS_TOKEN_URL, data=data)
    print(response.text)
    access_token = str.split(response.text, '&')
    access_token_key = str.split(access_token[0], '=')[1]
    access_token_secret = str.split(access_token[1], '=')[1]
    access_token_name = str.split(access_token[2], '=')[1]
    access_token_id = str.split(access_token[3], '=')[1]
    return {
            "access_token_key": access_token_key,
            "access_token_secret": access_token_secret ,
            "access_token_name": access_token_name,
            "access_token_id": access_token_id 
            }

# # Google Oauth
# @app.route("/google_login")
# def google_login():
#     google = OAuth2Session(Config.GOOGLE_CLIENT_ID, scope=Config.GOOGLE_CLIENT_ID)
#     authorization_url, state = google.authorization_url(Config.GOOGLE_AUTHORIZATION_URL)
#     session['oauth_state'] = state
#     return redirect(authorization_url)

# # Instagram Oauth
# @app.route("/instagram_login")
# def instagram_login():
#     instagram = OAuth2Session(Config.INSTAGRAM_CLIENT_ID, scope=Config.INSTAGRAM_CLIENT_ID)
#     authorization_url, state = instagram.authorization_url(Config.INSTAGRAM_AUTHORIZATION_URL)
#     session['oauth_state'] = state
#     return redirect(authorization_url)

api = Api(app)
CORS(app, resources=r'/*',allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Methods"])

initialize_routes(api)

jwt = JWTManager(app)

bcrypt = Bcrypt(app)
