from .base import BaseHandler
from lib.user_utils import check_secure_val

class WelcomeHandler(BaseHandler):
    def get(self):
        user_id = check_secure_val(self.get_cookie('user_id'))
        if user_id:
            self.write("Welcome," + user_id + "!")