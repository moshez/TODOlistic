import os
import json

class TODOItem(object):
    def __init__(self, due=None, title=None, notes=(), repeats=False, **kw):
        self.due = due # For now -- parse into seconds-since-epoch later
        self.title = title
        self.notes = notes
        self.repeats = bool(repeats)
        self.metadata = kw
    def __repr__(self):
        d = self.__dict__.copy()
        d.update(self.metadata)
        return 'TODOItem(%r)' % d

def readTODO(fname):
    rawData = json.load(file(fname))
    data = dict([(str(k), v) for k, v in rawData.iteritems()])
    return TODOItem(**data)

def readDirectory(dname):
    ret = dict()
    for fname in os.listdir(dname):
        fullFname = os.path.join(dname, fname)
        ret[fname] = readTODO(fullFname)
    return ret


