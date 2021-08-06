from src.api.user_api import UsersApi

def initialize_routes(api):
    api.add_resource(UsersApi, '/api') 