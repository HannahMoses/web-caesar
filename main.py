#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import caesar
class MainHandler(webapp2.RequestHandler):
    def get(self):
#What we are saying,name='message', is that, when this form gets submitted,I
#want the "HTTP   request, that is about to be sent out", to have a
#KEY VALUE pair, where the keyname is message and the value is, the content
# that is typed into this textarea
        textarea = "<textarea name ='message'></textarea>"
        submit = "<input  type ='submit'/>"
        form = "<form method ='post'>"+ textarea + "<br><br>"+submit +"</form>"
        self.response.write(form)

    def post(self):
        #To access the request from user that is coming
        # in from textarea when user hits submit button
        message = self.request.get("message")
#        message = "Hello"
        encrypted_message = caesar.encrypt(message,13)
        self.response.out.write("Secret message" + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
