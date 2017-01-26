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
import cgi #Common Gateway Interface is apretty old library in web back-end operations
def build_page(textarea_content):
    rotation_label = "<label style='color:rgb(198,12,100)'> Rotate by : </label>"
    rotation_input = "<input type ='number' name='rotation'/>"
    message_label = "<label style='color:rgb(198,12,100)'> Please enter a message : </label>"
#What we are saying,name='message', is that, when this form gets submitted,I
#want the "HTTP   request, that is about to be sent out", to have a
#KEY VALUE pair, where the keyname is message and the value is, the content
# that is typed into this textarea
    textarea = "<textarea name ='message'>" +textarea_content+ "</textarea>"
    submit = "<input  type ='submit'/>"
    form = ("<form style='background-color:rgb(240,200,255)' method ='post'>"+
            rotation_label + rotation_input +"<br><br>" +
            message_label + textarea + "<br><br>"+
            submit +
            "</form>")
    header = "<h2 style='color:rgb(198,12,100);background-color:rgb(240,200,255)'> Web Caesar</h2><br>"
    body = "<body style= 'background-color:rgb(200,200,255)'>WELCOME TO WEB CAESAR <br>You can now generate a secret <br>message, by entering a number,<br>by  which , each  alphabet in  your<br>text, will be rotated.  VOILA !!!</body>"+"<br>"
    return header + body + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")#parameter is empty strng since user has entered nothing right now
        self.response.write(content)
    def post(self):
        #To access the request from user that is coming
        # in from textarea when user hits submit button
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message,rotation)
        escaped_message = cgi.escape(encrypted_message)
        content = build_page(escaped_message)
        self.response.write(content)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
