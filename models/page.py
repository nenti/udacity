import datetime

class WikiPage(object):
    
    TABLE = 'blog'
    TYPE = 'WikiPage'

    def __init__(self, page_id, content, version=""):
        #self.id = str(int(time.time())) + "-" + str(uuid.uuid1()) #combine uuid and time to sort by time
        self.id = page_id + "#"
        self.content = content
        self.created = str(self._now())
        if version:
            self.id += version
        else:
            self.id += self.created

    @staticmethod
    def getHashKey():
        return WikiPage.TYPE
    
    def getRangeKey(self):
        return self.id
    
    def getData(self):
        data = {}
        data['content'] = self.content
        data['created'] = self.created
        return data
        
    def _now(self):
        return datetime.datetime.now()