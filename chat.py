from google.appengine.api import xmpp
from google.appengine.ext import webapp

def XMPP_handler(handler):
    class Wrapper(webapp.RequestHandler):
        def post(self):
            message = xmpp.Message(self.request.POST)
            handler(self.request, message)

class ChatHandler(webapp.RequestHandler):
    def post(self):
        message = xmpp.Message(self.request.POST)
        if message.body[0:5].lower() == 'hello':
            message.reply("Greetings!")