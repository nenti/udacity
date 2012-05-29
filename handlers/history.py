from handlers.base import BaseHandler
from models.page import WikiPage
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError
from boto.dynamodb.condition import BEGINS_WITH
import datetime


class HistoryHandler(BaseHandler):
    
    def get(self, page_id):
        
        table = self.db.get_table( WikiPage.TABLE )
        pages = []

        try:
            pages_ = table.query( WikiPage.getHashKey(), 
                                 range_key_condition = BEGINS_WITH(page_id + "#"),
                                 max_results=20, scan_index_forward=False)
        except DynamoDBKeyNotFoundError:
            pages = [{"content": "", "created": "", "Identifier": ""}]

        for page in list(pages_):
            new_data = page
            created = datetime.datetime.strptime(page["created"], "%Y-%m-%d %H:%M:%S.%f") # 2012-05-28 17:33:13.937911
            new_data["created"] = created.strftime("%a %b %d %H:%M:%S %Y")
            new_data["page_id"] = page["Identifier"].split("#")[0]
            new_data["version"] = page["Identifier"].split("#")[1]
            pages.append(new_data)
            

        self.render( "history.html", pages=pages, page_id=page_id ) 
    
    def post(self, page_id):
        pass