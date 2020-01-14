#!/usr/bin/env python
#
# Copyright 2011 fj.mail@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.dist import use_library
use_library('django', '1.2')

import logging
import os
import sys
import traceback
import wsgiref.handlers
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import testloader

# Set to True if stack traces should be shown in the browser, etc.
_DEBUG = True

class FrontPageHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            vars = {'user': user,
                    'logout_url': users.create_logout_url('/'),
                    }
        else:
            vars = {'login_url': users.create_login_url(self.request.uri),
                    }
        vars['text'] = testloader.main()
        rendered = webapp.template.render('templates/yhbt.html', vars, debug=_DEBUG)
        self.response.out.write(rendered)

def main():
    application = webapp.WSGIApplication([
            ('/', FrontPageHandler),
#            ('/_ah/xmpp/message/chat/', XMPPHandler),
            ],
            debug=_DEBUG)
    wsgiref.handlers.CGIHandler().run(application)
    
if __name__ == '__main__':
    main()
