from flask_restful import Api
from flask import Flask
from flask_bcrypt import Bcrypt
import os
from flask_jwt_extended import JWTManager
from src.routes.routes import initialize_routes
from config import Config
from flask_cors import CORS

# Place where app is defined
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
CORS(app, resources=r'/*',allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Methods"])

initialize_routes(api)

jwt = JWTManager(app)

bcrypt = Bcrypt(app)
