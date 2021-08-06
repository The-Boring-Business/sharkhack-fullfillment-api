from Astra.pyastra.types.table import Table
from Astra.pyastra.tables import Tables

def create_user():
        T = Table("user")
        T.add_columns("username", "text", isPrimaryKey=True)
        T.add_columns("email", "text",isPrimaryKey=True)
        T.add_columns("password", "text")
        T.add_columns("display_name", "text")
        T.add_columns("DOB", "timestamp")
        T.add_columns("niche", "text")
        T.add_columns("avatar", "blob")
        DB = Tables('bot')
        res = DB.add_table(T)
        return res

def delete_user():
        DB = Tables('bot')
        res = DB.delete_table('user')
        return res.json()