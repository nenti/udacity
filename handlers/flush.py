from .base import BaseHandler

class FlushHandler(BaseHandler):
    def get(self):
        self.CACHE.clear()
        self.redirect( "/")