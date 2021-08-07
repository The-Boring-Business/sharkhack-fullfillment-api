from model.user import User
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from requests_oauthlib import OAuth1Session
from config import Config



class Twitter_Api(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        res = user.save()
        return User