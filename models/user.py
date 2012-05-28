import datetime
import uuid

class User(object):
    
    TABLE = 'blog'
    TYPE = 'Users'
    
    def __init__(self, username, password, email=""):
        self.id = uuid.uuid1()
        self.username = username
        self.password = password
        self.email=email
        self.created = str(self._now())
    
    def getHashKey(self):
        return self.TYPE
    
    def getRangeKey(self):
        return str(self.username)
    
    def getData(self):
        data = {}
        data['username'] = self.username
        data['password'] = self.password
        if self.email:
            data['email'] = self.email
        return data
    
    def _now(self):
        return datetime.datetime.now()