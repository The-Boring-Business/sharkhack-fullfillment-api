import requests
from Astra.pyastra.types.credits import Credits
import json

class Tables(Credits):
    def __init__(self):
        self.base = "https://"+self.ID+"-"+ self.Region +".apps.astra.datastax.com/api/rest/v2/schemas/keyspaces/"+self.keyspace

    def get_all_tables(self):
        url = self.base+"/tables"
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()

    def add_table(self, table):
        url = self.base+"/tables"
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        body = {
            "name": table.name,
            "columnDefinitions" : [],
            "ifNotExists": True,
            "primaryKey": {
                "partitionKey": []
            }
        }
        for column in table.columns:
            body["columnDefinitions"].append({"name": column.name, "typeDefinition": column.type, "static": column.static})
        for pk in table.columns:
            if pk.isPrimaryKey:
                body["primaryKey"]["partitionKey"].append(pk.name)
        r = requests.post(url, data=json.dumps(body), headers=query)
        return r.json()
    
    def delete_table(self, tablename):
        url = self.base+"/tables/"+tablename
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.delete(url, headers=query)
        return r.json()

    def get_table(self, tablename):
        url = self.base+"/tables/"+tablename
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()
    
    def get_all_columns(self, tablename):
        url = self.base+"/tables/"+tablename+"/columns"
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()

    def get_column(self, tablename, columnname):
        url = self.base+"/tables/"+tablename+"/columns/"+columnname
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()
    
    def update_column_name(self, tablename, column, newname):
        if column.isPrimaryKey:
            url = self.base+"/tables/"+tablename+"/column/"+column.name
            query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
            body = {
                "name": newname,
                "typeDefinition": column.type,
                "static": column.static
            }
            r = requests.put(url, data=json.dumps(body), headers=query)
            return r.json()
        return "Sorry you can only update a Primary Key Column"


    def get_indexes(self, tablename):
        url = self.base+"/tables/"+tablename+"/indexes"
        query = {'X-Cassandra-Token':self.Token, 'Content-Type':'application/json', "Accept": "application/json"}
        r = requests.get(url, headers=query)
        return r.json()
        
