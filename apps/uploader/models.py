
class File():

    fields = [ 'id',
               'name',
               'filename',
               'description'
             ]

    def __init__(self, rdb):
        """ param rdb: instance of redis.Redis class
        """
        self.rdb = rdb

    def init(self):
        """perform some initialization
        """

    def create(self):



    def __repr__(self):
        return "<Entity('%d', '%s')>" % (self.id, self.name)

