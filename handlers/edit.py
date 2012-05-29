import tornado

from .base import BaseHandler
from models import WikiPage
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError
from boto.dynamodb.condition import BEGINS_WITH

class EditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, page_id):
        
        version = self.get_argument( "v", default="" )
        identifier = page_id + "#" + version
        table = self.db.get_table( WikiPage.TABLE )

        if self.CACHE.has_key(identifier):
            page = self.CACHE[identifier]
        else:
            page = table.query( WikiPage.getHashKey(), 
                                 range_key_condition = BEGINS_WITH(page_id + "#" + version),
                                 max_results=1, scan_index_forward=False)
            page = list(page)
            if page:
                page = page.pop()
            else:
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
        self.CACHE[page_id + "#"] = page.getData()
        self.redirect( page_id )