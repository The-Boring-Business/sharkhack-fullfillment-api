import os

class Config:
    ASTRA_DB_ID = os.environ.get('ASTRA_DB_ID')
    ASTRA_DB_REGION = os.environ.get('ASTRA_DB_REGION')
    ASTRA_DB_KEYSPACE= os.environ.get('ASTRA_DB_KEYSPACE')
    ASTRA_DB_TOKEN = os.environ.get('ASTRA_DB_APPLICATION_TOKEN')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
    TWITTER_SECRET = os.environ.get('TWITTER_SECRET')
    TWITTER_CALLBACK = os.environ.get('CALLBACK')
