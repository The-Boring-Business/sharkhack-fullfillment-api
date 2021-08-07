from flask import Flask, Response, request
from flask_restful import Resource
from model.user import User


class UsersApi(Resource):
  def get(self, username):
    " get user details based on username"
    user = User.get_user_details(username)
    return str(user)
  def post(self, username):
    " update user details based on username"
    body = request.get_json()
    user = User.update_data(username, body)
    return str(user)
    

