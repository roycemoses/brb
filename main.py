#main.py
# the import section
import webapp2
import os
import json
import random
import jinja2

from google.appengine.api import urlfetch

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class StartPage(webapp2.RequestHandler):
    def get(self):
        start_page_template = JINJA_ENVIRONMENT.get_template('templates/gameplay.html')

        user_current_room = self.request.get('current-room')

        user_current_room_dict = {
            "current_room": user_current_room
        }

        self.response.write(start_page_template.render(user_current_room_dict))

    # def post(self):
        # to do: get current room from hidden input and user action


# class CreateCharacterPage(webapp2.RequestHandler):
#     def post(self):
#         create_character_template = JINJA_ENVIRONMENT.get_template('templates/createcharacter.html')
#         self.response.write(create_character_template.render())
#
# class GameplayPage(webapp2.RequestHandler):
#     def post(self):
#         game_page_template = JINJA_ENVIRONMENT.get_template('templates/gameplay.html')
#
#         usernameinput = self.request.get('user-name')
#
#         name_dict = {
#              "user_name": usernameinput
#          }
#
#         self.response.write(game_page_template.render(name_dict))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/', StartPage),
], debug=True)
