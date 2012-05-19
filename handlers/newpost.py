import tornado
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
            table = self.db.get_table(blogpost.table)
            item_data = {
                         'content': blogpost.content,
                         'created': blogpost.created
            }
            item = table.new_item(
                hash_key = 'Posts',
                range_key = blogpost.subject,
                attrs = item_data
            )
            item.put()
            self.redirect("/%s" % subject)
        else:
            error = "Subject and Content are required to save the blogpost"
            self.render("newpost.html", subject = subject, content = content, error = error)