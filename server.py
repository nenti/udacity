import os

import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers import IndexHandler
from handlers import NewpostHandler
from handlers import SignupHandler
from handlers import LogoutHandler
from handlers import LoginHandler
from handlers import WelcomeHandler
from server_config import site_config
from db import ConnectDB

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/signup', SignupHandler),
            (r'/logout', LogoutHandler),
            (r'/login', LoginHandler),
            (r'/welcome', WelcomeHandler),
            (r'/newpost', NewpostHandler),
            (r'/(?:([^.]+)|(.json))*', IndexHandler),
        ]
        settings = {
            'site_title' : site_config["site_title"], 
            'login_url' : '/login', 
            'template_path' : os.path.join(os.path.dirname(__file__), 'tpl'), 
            'static_path' : os.path.join(os.path.dirname(__file__), "static"),
            'xsrf_cookies' : False, 
            'cookie_secret' : '3295bfab668c4ad48dad43f890402905',
            'google_analytics' : site_config["google_analytics"], 
            'feed_url' : site_config["feed_url"],
            'debug': True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = ConnectDB()

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(site_config['server_port'])
    tornado.ioloop.IOLoop.instance().start()