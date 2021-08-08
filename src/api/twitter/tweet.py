from flask_restful import Resource
from flask import request
from src.api.twitter.setup import setup_api
import requests
import base64
import io
from PIL import Image

class Twitter_Api(Resource):
    def post(self):
        body = request.get_json()
        access_token = body['access_token']
        access_token_secret = body['access_token_secret']
        api = setup_api(access_token, access_token_secret)
        data = body['test_data']
        if 'image_url' in body.keys():
            image = body['image_url']
            status = api.update_status(status=data+" " + image)
        if 'image' in body.keys():
            image = body['image']
            mediaid = api.media_upload("imageToSave.png")
            status = api.update_with_media("imageToSave.png", status=data)
            
            #update status with image
        else:
            status = api.update_status(status=data)
        return {'status': 'success'}
