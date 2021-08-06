from Astra.pyastra.types.columns import Column



class Table:
    """ Cassendra table object 
    """
    def __init__(self, name):
        self.name = name
        self.columns = []

    def __repr__(self):
        return "Table(%s, %s)" % (self.name, self.columns)

    def __str__(self):
        return "Table(%s, %s)" % (self.name, self.columns)
    
    def add_columns(self, name, type,is_static = False, isPrimaryKey = False):
        column = Column(name, type) 
        if isPrimaryKey:
            column.set_primary_key(isPrimaryKey)
        if is_static:
            column.set_static(is_static)
        if column not in self.columns:
            self.columns.append(column)
        else:
            raise Exception("Column already exists")
    def get_cols(self):
        return self.columns


