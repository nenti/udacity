import tornado

from .base import BaseHandler
from models import WikiPage
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError

class EditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, page_id):
        
        table = self.db.get_table( WikiPage.TABLE )

        try:
            page = table.get_item( WikiPage.getHashKey(), page_id )
        except DynamoDBKeyNotFoundError:
            page = {"content": ""}

        self.render( "edit.html", page=page )
    
    @tornado.web.authenticated
    def post(self, page_id):
        content = self.get_argument( "content", default="" )

        page = WikiPage( page_id = page_id, content = content )
        table = self.db.get_table( WikiPage.TABLE )
        item = table.new_item(
            hash_key = page.getHashKey(),
            range_key = page.getRangeKey(),
            attrs = page.getData()
        )
        item.put()
        self.redirect( page_id )