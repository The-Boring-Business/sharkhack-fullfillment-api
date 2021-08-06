from flask import Flask, Response, request
from flask_restful import Resource
from model.user import User


class UsersApi(Resource):
  def get():
    pass