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
        rotation_label = "<label style='color:rgb(198,12,100)'> Rotate by : </label>"
        rotation_input = "<input type ='number' name='rotation'/>"
        message_label = "<label style='color:rgb(198,12,100)'> Please enter a message : </label>"
#What we are saying,name='message', is that, when this form gets submitted,I
#want the "HTTP   request, that is about to be sent out", to have a
#KEY VALUE pair, where the keyname is message and the value is, the content
# that is typed into this textarea
        textarea = "<textarea name ='message'></textarea>"
        submit = "<input  type ='submit'/>"
        form = ("<form style='background-color:rgb(240,200,255)' method ='post'>"+
                rotation_label + rotation_input +"<br><br>" +
                message_label + textarea + "<br><br>"+
                submit +
                "</form>")
        header = "<h2 style='color:rgb(198,12,100);background-color:rgb(240,200,255)'> Web Caesar</h2><br>"
#        body = "<body style="background-color:powderblue;"></body>"
#        self.response.write(header + body+form)
        self.response.write(header + form)
    def post(self):
        #To access the request from user that is coming
        # in from textarea when user hits submit button
        message = self.request.get("message")
        rotation = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message,rotation)
        self.response.out.write("Secret message : " + encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
