from .base import BaseHandler
from models import WikiPage
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError
from boto.dynamodb.condition import BEGINS_WITH

LIST_CACHE_KEY = "list_cache"
ENTRY_CACHE_KEY = "entry_cache"

class WikiHandler(BaseHandler):
    def get(self, page_id):
        
        version = self.get_argument( "v", default="" )
        identifier = page_id + "#" + version
        
        table = self.db.get_table( WikiPage.TABLE )

        if self.CACHE.has_key(identifier):
            page = self.CACHE[identifier]
            hit = "False"
        else:
            page = table.query( WikiPage.getHashKey(), 
                                 range_key_condition = BEGINS_WITH(page_id + "#" + version),
                                 max_results=1, scan_index_forward=False)
            page = list(page)
            hit = "True"
            if page:
                page = page.pop()
                self.CACHE[identifier] = page
        
        if page:
            self.render( "wiki_page.html", page = page, hit=hit )
        else:
            self.redirect( "/_edit" + page_id )
        
        
        

        


            
            
#class WelcomePage(webapp2.RequestHandler):
#    def get(self):
#        user_id = check_secure_val(self.request.cookies.get('user_id'))
#        if user_id:
#            current_user = User.get_by_id(int(user_id))
#            self.response.out.write("Welcome," + current_user.username + "!")
#        else:
#            self.redirect("/signup")