from .base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self, post_id, print_json):

        table = self.db.get_table('blog')
        if post_id:
            posts = table.get_item('Posts', post_id)
            posts_ = [posts] #for homework evaluation
        else:
            posts = list(table.query('Posts', max_results=10, scan_index_forward=False))
            posts_ = posts #for homework evaluation
            
        if print_json:
            self.return_json(posts)
        else:
            self.render("blog.html", posts = posts_)
            
#class WelcomePage(webapp2.RequestHandler):
#    def get(self):
#        user_id = check_secure_val(self.request.cookies.get('user_id'))
#        if user_id:
#            current_user = User.get_by_id(int(user_id))
#            self.response.out.write("Welcome," + current_user.username + "!")
#        else:
#            self.redirect("/signup")