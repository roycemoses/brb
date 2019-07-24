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
        start_page_template = JINJA_ENVIRONMENT.get_template('templates/startpage.html')

        self.response.write(start_page_template.render())


class CreateCharacterPage(webapp2.RequestHandler):
    def post(self):
        create_character_template = JINJA_ENVIRONMENT.get_template('templates/createcharacter.html')
        self.response.write(create_character_template.render())


class GameplayPage(webapp2.RequestHandler):
    def post(self):
        game_page_template = JINJA_ENVIRONMENT.get_template('templates/gameplay.html')

        usernameinput = self.request.get('user-name')

        name_dict = {
            "user_name": usernameinput
        }

        self.response.write(game_page_template.render(name_dict))

class Event1(webapp2.RequestHandler):
    def post(self):
        room1_page_template = JINJA_ENVIRONMENT.get_template('templates/room1.html')
        room2_page_template = JINJA_ENVIRONMENT.get_template('templates/room2.html')
        game_page_template = JINJA_ENVIRONMENT.get_template('templates/gameplay.html')

        usernameinput = self.request.get('user-name')

        name_dict = {
            "user_name": usernameinput
        }

        room_input = self.request.get('room-type')

        def chooseRoom():
            if (room_input == "1"):
                self.response.write(room1_page_template.render())
            elif (room_input == "2"):
                self.response.write(room2_page_template.render())
            elif room_input != "1" or room_input != "2":
                self.response.write(game_page_template.render())

        chooseRoom()

# class EditMemeHandler(webapp2.RequestHandler):
#     def get(self):
#         meme_key_string = self.request.get('meme-key')
#         meme_key = ndb.(urlsafe=meme_key_string)
#         meme = meme_key.get()
#         # ^ This meme is an object for the type meme.
#         user = users.get_current_user() #get the current logged in users
#         if meme.creator != user.user_id():
#             # do something bad
#             pass
#         else:
#             meme.top_text = self.request.get('top_text')
#             meme.middle_text = self.request.get('middle_text')
#             meme.bottom_text = self.request.get('bottom_text')
#             meme.put()
#
# class UserProfile(webapp2.RequestHandler):
#     user_id = ndb.StringProperty(required=true)
#     game_nickname = ndb.StringProperty(required=true)
#     favorite_color = ndb.StringProperty(required=true)
#     style_preferences = ndb.StringProperty(required=true)
#
#
#
#         if memes:
#             latest_meme_key = memes[0].key.urlsafe()
#         else:
#             latest_meme_key = ""
#         for meme in memes:



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', StartPage),
    ('/createcharacter', CreateCharacterPage),
    ('/gameplay', GameplayPage),
    ('/event1', Event1),
], debug=True)
