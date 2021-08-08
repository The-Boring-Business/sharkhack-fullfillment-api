from Astra.pyastra.types.table import Table
from Astra.pyastra.tables import Tables

def create_user():
        T = Table("user")
        T.add_columns("username", "text", isPrimaryKey=True)
        T.add_columns("email", "text")
        T.add_columns("password", "text")
        T.add_columns("display_name", "text")
        T.add_columns("DOB", "timestamp")
        T.add_columns("niche", "text")
        T.add_columns("avatar", "text")
        DB = Tables('bot')
        res = DB.add_table(T)
        return res
def create_post():
        T = Table("Post")
        T.add_columns("username", "text", isPrimaryKey=True)
        T.add_columns("content", "text")
        T.add_columns("time", "text")
        T.add_columns("type", "text")
        DB = Tables()
        res = DB.add_table(T)
        return res
def create_user_post():
        T = Table("userpost")
        T.add_columns("username", "text", isPrimaryKey=True)
        T.add_columns("Time", "text")
        DB = Tables()
        res = DB.add_table(T)
        return res

def delete_user():
        DB = Tables()
        res = DB.delete_table('user')
        return res.json()

def delete_post():
        DB = Tables()
        res = DB.delete_table('Post')
        return res.json()


