from os import stat
from Astra.pyastra.data import Data
from flask_bcrypt import generate_password_hash, check_password_hash
from collections import OrderedDict

DB = Data('userpost')

class Userpost(object):
    def __init__(self, username = None, Time=""):
        self.username = username
        self.Time = Time
        self.data = {
        "username" : self.username,
        "Time" : self.Time,
    }
        
    def __repr__(self) -> str:
        return str(dict(sorted(self.data.items())))
        

    def save(self): 
        d =  DB.insert_data(self.data)   
        return dict(sorted(d.items()))
    
    @staticmethod
    def add_timestamp(username,stamp):
        data = DB.get_row_by_primarykey(username)
        data['data'][0]['Time'] += ","+stamp
        data['data'][0].pop('username')
        try:
            DB.update_row(username, data)
            return True
        except:
            return False


    @staticmethod
    def get_post_details(username):
        data = DB.get_row_by_primarykey(username)
        return  dict(sorted(data.items()))

    @staticmethod
    def delete_post(username):
        if DB.delete_row_by_primary_key(username):
            return "sucess"
        return 'failed'
