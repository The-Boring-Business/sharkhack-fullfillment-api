from os import stat
from Astra.pyastra.data import Data
from flask_bcrypt import generate_password_hash, check_password_hash
from collections import OrderedDict

DB = Data('user')

class User(object):
    def __init__(self, username = None, password = "", email=None, display_name=None):
        self.username = username
        self.password = password
        self.email = email
        self.display_name = display_name
        self.data = {
        "username" : self.username,
        "password" : self.password,
        "email" : self.email,
    }
        
    def __repr__(self) -> str:
        return str(dict(sorted(self.data.items())))
    
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
        self.data['password'] = self.password

    @staticmethod
    def check_password(old, password):
        return check_password_hash(old, password)
    
    def set_data(self, username, password, email):
        self.username = username
        self.password = self.hash_password(password)
        self.email = email
    
    def set_avatar(self, image_data):
        self.data["avatar"] = str(image_data)
    
    def set_display_name(self, display_name):
        self.data["display_name"] = display_name

    def set_niche(self, niche):
        self.data["niche"] = niche
    
    def set_dob(self, dob):
        self.data["DOB"] = dob

    def save(self): 
        d =  DB.insert_data(self.data)   
        return dict(sorted(d.items()))

    @staticmethod
    def get_user_details(username):
        data = DB.get_row_by_primarykey(username)
        data = data['data'][0]
        data.pop('password')
        return  dict(sorted(data.items()))
    
    @staticmethod
    def update_data(username, data):
        try:
            DB.update_row(username, data)
            return True
        except:
            return False