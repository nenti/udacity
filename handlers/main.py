from .base import BaseHandler

LIST_CACHE_KEY = "list_cache"
ENTRY_CACHE_KEY = "entry_cache"

class IndexHandler(BaseHandler):
    def get(self, post_id, print_json):

        table = self.db.get_table('blog')
        if post_id:
            key = ENTRY_CACHE_KEY + str(post_id)
            if key in self.CACHE:
                posts_ = [self.CACHE[key]]
                query_time = self.CACHE.getDelta(key)
            else:
                self.CACHE[key] = table.get_item('Posts', post_id)
                posts_ = [self.CACHE[key]]
                query_time = self.CACHE.getDelta(key)
            posts = self.CACHE[key]
        else:
            if LIST_CACHE_KEY in self.CACHE:
                posts_ = self.CACHE[LIST_CACHE_KEY]
                query_time = self.CACHE.getDelta(LIST_CACHE_KEY)
            else:
                self.CACHE[LIST_CACHE_KEY] = list(table.query('Posts', max_results=10, scan_index_forward=False))
                posts_ = self.CACHE[LIST_CACHE_KEY]
                query_time = self.CACHE.getDelta(LIST_CACHE_KEY)
            posts = posts_
                            
        if print_json:
            self.return_json(posts)
        else:
            self.render("blog.html", posts = posts_, query_time = query_time)
            
#class WelcomePage(webapp2.RequestHandler):
#    def get(self):
#        user_id = check_secure_val(self.request.cookies.get('user_id'))
#        if user_id:
#            current_user = User.get_by_id(int(user_id))
#            self.response.out.write("Welcome," + current_user.username + "!")
#        else:
#            self.redirect("/signup")