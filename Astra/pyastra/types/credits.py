import requests
from config import Config

class Credits:
        ID = Config.ASTRA_DB_ID
        Region = Config.ASTRA_DB_REGION
        Token = Config.ASTRA_DB_TOKEN
        keyspace = Config.ASTRA_DB_KEYSPACE