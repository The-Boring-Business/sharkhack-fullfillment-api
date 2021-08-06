class Column:
    """ Cassandra column object
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.static = False
        self.isPrimaryKey = False
    def __repr__(self):
        if self.isPrimaryKey:
            return "Column(%s, %s, PK)" % (self.name, self.type)
        return "Column (%s, %s)" % (self.name)
    def __str__(self):
        if self.isPrimaryKey:
            return "Column(%s, %s, PK)" % (self.name, self.type)
        return "Column (%s, %s)" % (self.name)
    def __hash__(self):
        return hash((self.name))
    def __eq__(self, other):
        try:
            return ( self.name) == ( other.name)
        except AttributeError:
            return "NotImplemented"
    def set_static(self, static):
        # check if static is of type Boolen
        if not isinstance(static, bool):
            raise Exception("Static must be of type Boolean")
        self.static = static
    def set_primary_key(self, is_primary_key):
        # check if static is of type Boolen
        if not isinstance(is_primary_key, bool):
            raise Exception("Primary Key must be of type Boolean")
        self.isPrimaryKey = is_primary_key
