import re
from .base import BaseHandler
from models import User
from lib.user_utils import make_pw_hash, make_secure_val

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

class SignupHandler(BaseHandler):
    
    def get(self):
        self.render("signup.html",  username="", 
                                    username_error="", 
                                    password_error="", 
                                    email="", 
                                    email_error="" )
    
    def post(self):
        username = check_match(USER_RE, self.get_argument('username', default=""))
        password = check_match(PASSWORD_RE, self.get_argument('password', default=""))
        verify = check_match(PASSWORD_RE, self.get_argument('verify', default=""))
        email = check_match(EMAIL_RE, self.get_argument('email',default=""))
        
        username_error = validate_uname(username)
        password_error = validate_password(password, verify)
        email_error = validate_email(email)
        
        if username_error or password_error:
            self.render("signup.html",    username=username, 
                                        username_error=username_error, 
                                        password_error=password_error, 
                                        email=email, 
                                        email_error=email_error)
        else:
            hash = make_pw_hash(username, password)
            new_user = User(username = username, password = hash)
            table = self.db.get_table(User.TABLE)
            item = table.new_item(
                hash_key = new_user.getHashKey(),
                range_key = new_user.getRangeKey(),
                attrs = new_user.getData()
            )
            item.put()
            self.set_cookie("user_id", str(make_secure_val(new_user.getRangeKey())))
            self.redirect("/welcome")


def check_match(regexp, value):
    matchobj = regexp.match(value)
    
    if matchobj:
        return matchobj.group(0)
    else:
        return ""

def validate_uname(username):
    if not username:
        return "Username not vaild"
    else:
        return ""
    
def validate_password(password, verify):
    if not password:
        return "Password invalid"
    elif password != verify: 
        return "Passwords don't match"
    else:
        return ""
    
def validate_email(email):
    if not email:
        return "Email not vaild"
    else:
        return ""
    
