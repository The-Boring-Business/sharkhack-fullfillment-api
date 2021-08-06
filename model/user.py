from Astra.pyastra.data import Data
from flask_bcrypt import generate_password_hash, check_password_hash
import base64
from imageio import imread, get_reader
from  config import Config

class User(object):
    #data = Data('user')
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.display_name = username
        self.avatar = Config.AVATAR_DEFAULT
        self.niche = ""
        self.DOB = ""
        self.data = {"username" : self.username,
        "password" : self.password,
        "email" : self.email,
        "display_name" : self.display_name,
        "avatar" : self.avatar,
        "niche" : self.niche,
        "DOB" : self.DOB
    }
        
    def __repr__(self) -> str:
        return str(self.data)
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def set_data(self, username, password, email):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email
    
    def set_avatar(self, image_data):
        if type(image_data) is not bytes:
            image_data = base64.b64encode(image_data)
        self.avatar = image_data
    
    def set_niche(self, niche):
        self.niche = niche
    
    def set_dob(self, dob):
        self.DOB = dob
    def save(self):
        data = {
        "username" : self.username,
        "password" : self.password,
        "email" : self.email,
        "display_name" : self.display_name,
        "avatar" : self.avatar,
        "niche" : self.niche,
        "DOB" : self.DOB
             }       
        D = Data('user')
        return D.insert_data(data)
        
