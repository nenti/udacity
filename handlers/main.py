from .base import BaseHandler
from models import WikiPage
from boto.dynamodb.exceptions import DynamoDBKeyNotFoundError

LIST_CACHE_KEY = "list_cache"
ENTRY_CACHE_KEY = "entry_cache"

class WikiHandler(BaseHandler):
    def get(self, page_id):

        table = self.db.get_table( WikiPage.TABLE )
        
        try:
            page = table.get_item( WikiPage.getHashKey(), page_id )
            self.render( "wiki_page.html", page = page )
        except DynamoDBKeyNotFoundError:
            self.redirect( "/_edit" + page_id )

        


            
            
#class WelcomePage(webapp2.RequestHandler):
#    def get(self):
#        user_id = check_secure_val(self.request.cookies.get('user_id'))
#        if user_id:
#            current_user = User.get_by_id(int(user_id))
#            self.response.out.write("Welcome," + current_user.username + "!")
#        else:
#            self.redirect("/signup")