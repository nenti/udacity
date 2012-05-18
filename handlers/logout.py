from .base import BaseHandler

class LogoutHandler(BaseHandler):
    def get(self):
        self.set_cookie("user_id", "")
        self.redirect("/signup")