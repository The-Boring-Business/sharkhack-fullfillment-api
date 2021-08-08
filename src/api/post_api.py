from flask import Flask, Response, request
from flask_restful import Resource
from model.post import Post



class PostApi(Resource):
  def get(self, username):
    " get user details based on username"
    user = Post.get_post_details(username)
    return str(user['data'])

  def post(self, username):
        body = request.get_json()
        post = Post(**body)
        res = post.save()
        return str(res), 200
  def delete(self,username):
    try:
      Post.delete_post('anushkrishnav')
    except ValueError:
      return 'done'
