import datetime
import uuid
import time

class Blogpost(object):
    
    TABLE = 'blog'
    TYPE = 'Posts'

    def __init__(self, subject, content):
        self.id = str(int(time.time())) + "-" + str(uuid.uuid1()) #combine uuid and time to sort by time
        self.subject = subject
        self.content = content
        self.created = str(self._now())

    def getHashKey(self):
        return self.TYPE
    
    def getRangeKey(self):
        return self.id
    
    def getData(self):
        data = {}
        data['subject'] = self.subject
        data['content'] = self.content
        data['created'] = self.created
        return data
        
    def _now(self):
        return datetime.datetime.now()