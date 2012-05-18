import datetime

class Blogpost(object):
    def __init__(self, subject, content):
        self.table = 'blog'
        self.subject = subject
        self.content = content
        self.created = str(self._now())
        
    def _now(self):
        return datetime.datetime.now()