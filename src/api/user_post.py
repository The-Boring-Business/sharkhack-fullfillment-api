from flask import Flask, Response, request
from flask_restful import Resource
from model.user_post import Userpost


class UsersApi(Resource):
  def get(self, username):
    " get user details based on username"
    user = Userpost.get_post_details(username)
    return str(user['data'])
  def post(self, username):
        body = request.get_json()
        
        post = Userpost(**body)
        res = post.save()
        return str(res), 200

