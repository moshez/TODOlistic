from todolistic import reader

class DB(object):
    def __init__(self, dname):
        self.dname = dname
        self.contents = reader.readDirectory(dname)
    def __getitem__(self, uuid):
        return self.contents[uuid]
    def __setitem__(self, uuid):
        raise NotImplementedError("not yet")
