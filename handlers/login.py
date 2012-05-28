from .base import BaseHandler
from models import User
from lib.user_utils import valid_pw, make_secure_val

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", login_error="", username="")
    
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        
        table = self.db.get_table(User.TABLE)
        cur_user = table.get_item(User.TYPE, username)
        if cur_user and valid_pw(username, password, cur_user['password']):
            self.set_cookie("user_id", str(make_secure_val(cur_user['username'])))
            self.redirect("/")
        else:
            self.render("login.html", login_error="login failed", username=username)