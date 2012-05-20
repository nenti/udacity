import tornado
import urllib
import urlparse
from tornado.escape import utf8

from .base import BaseHandler
from models import Blogpost

class NewpostHandler(BaseHandler):
    def get(self):
        self.render("newpost.html", subject="", content="", error="")
    
    def post(self):
        subject = self.get_argument("subject", default="")
        content = self.get_argument("content", default="")
        
        if subject and content:
            blogpost = Blogpost(subject = subject, content = content)
            table = self.db.get_table(Blogpost.TABLE)
            item = table.new_item(
                hash_key = blogpost.getHashKey(),
                range_key = blogpost.getRangeKey(),
                attrs = blogpost.getData()
            )
            item.put()
            self.redirect( "/%s" % urllib.quote(blogpost.getRangeKey()) )
        else:
            error = "Subject and Content are required to save the blogpost"
            self.render("newpost.html", subject = subject, content = content, error = error)