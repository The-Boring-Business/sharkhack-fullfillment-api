from src.api.user_api import UsersApi
from src.api.post_api import PostApi
from src.api.twitter.tweet import Twitter_Api
from src.api.auth_api import SignupApi, LoginApi

def initialize_routes(api):

    # GET: get user details based on username
    # POST : Update user details based on username
    api.add_resource(UsersApi, '/api/<username>') 
    api.add_resource(PostApi, '/api/post/<username>') 
    
    # POST 
    api.add_resource(LoginApi, '/api/login') 
    # POST 
    api.add_resource(SignupApi, '/api/register') 
    
    # POST
    api.add_resource(Twitter_Api, '/api/tweet/')
