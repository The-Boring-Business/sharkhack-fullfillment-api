import requests
from Astra.pyastra.types.credits import Credits
import json

class Data(Credits):
    """
    Class to handle data requests.
    """
    def __init__(self, tablename):
        self.base = "https://"+self.ID+"-"+ self.Region +".apps.astra.datastax.com/api/rest/v2/keyspaces/"+self.keyspace+'/'+tablename

    def get_all_rows(self):
        url = self.base+"/rows"
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()
    def insert_data(self, data):
        url = self.base
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.post(url, data=json.dumps(data), headers=query)
        return r.json()
    
    def update_row(self, primarykey, data):
        url = self.base+"/"+primarykey
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.patch(url, data=json.dumps(data), headers=query)
        return r.json()

    def get_row_by_primarykey(self,primarykey):
        if type(primarykey) is list:
            url = self.base+"/"+"/".join(primarykey)
        else : 
            url = self.base+"/"+primarykey
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()
    
    def get_row_by_composite_key(self,compositekeys):
        key = "/".join(compositekeys)
        url = self.base+"/"+key
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()

    def delete_row_by_primary_key(self,primarykey):
        if type(primarykey) is list:
            url = self.base+"/"+"/".join(primarykey)
        else : 
            url = self.base+"/"+primarykey
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.delete(url, headers=query)
        return r.json()
    
    def delete_row_by_composite_key(self,compositekeys):
        key = "/".join(compositekeys)
        url = self.base+"/"+key
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.delete(url, headers=query)
        return r.json()
    
    def search_table(self, search_string):
        pass