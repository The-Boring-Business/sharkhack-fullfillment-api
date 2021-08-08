from os import stat
from Astra.pyastra.data import Data
from flask_bcrypt import generate_password_hash, check_password_hash
from collections import OrderedDict

DB = Data('Post')

class Post(object):
    def __init__(self, username = None, content = "", time=None, date=None, type=None):
        self.username = username
        self.content = content
        self.time = time
        self.type = type
        self.data = {
        "username" : self.username,
        "content" : self.content,
        "time" : self.time,
        "type" : self.type
    }
        
    def __repr__(self) -> str:
        return str(dict(sorted(self.data.items())))
        

    def save(self): 
        d =  DB.insert_data(self.data)   
        return dict(sorted(d.items()))

    @staticmethod
    def get_post_details(username):
        data = DB.get_row_by_primarykey([username])
        return  dict(sorted(data.items()))
    
    @staticmethod
    def delete_post(username):
        if DB.delete_row_by_primary_key([username]):
            return "sucess"
        return 'failed'