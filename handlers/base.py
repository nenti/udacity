import tornado.web
import urlparse
from lib.user_utils import check_secure_val
from tornado.escape import utf8
from lib.cache import Cache

class BaseHandler(tornado.web.RequestHandler):
    
    CACHE = Cache()
    
    @property
    def db(self):
        return self.application.db
    
    def return_json(self, data_dict):
        """
        acessory method to return json objects
        """
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        json_ = tornado.escape.json_encode(data_dict)
        self.write(json_)
        self.finish()
        
    def get_current_user(self):
        user_id = check_secure_val(self.get_cookie('user_id'))
        if user_id:
            return user_id
        
    def redirect(self, url, **kwargs):
        """
        Turns the relative redirect path of the redirect statement into an absolute one to 
        work with udacity's googleappengine http client
        """
        url = urlparse.urljoin(utf8(self.request.protocol + "://" + self.request.host),url)
        super( BaseHandler, self ).redirect(url, **kwargs)
        
        #http://77.176.250.245:8080/