from flask import request
from model.user import User
from flask_restful import Resource
from flask import Response, request
from flask_jwt_extended import create_access_token
import datetime

class SignupApi(Resource):
 def post(self):
   body = request.get_json()
   user = User(**body)
   user.hash_password()
   res = user.save()
   return str(res), 200

class LoginApi(Resource):
 def post(self):
   body = request.get_json()
   user = User.get_data(username=body.get('username'))
   authorized = User.check_password(user['password'],body.get('password'))
   if not authorized:
     return {'error': 'Email or password invalid'}, 401
   expires = datetime.timedelta(days=1)
   access_token = create_access_token(identity=str(user['username']), expires_delta=expires)
   return {'token': access_token}, 200
