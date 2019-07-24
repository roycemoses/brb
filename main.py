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

        room_input = self.request.get('room-type')
        def chooseRoom():
            if (room_input == "1"):
                self.response.write(room1_page_template.render())
            elif (room_input == "2"):
                self.response.write(room2_page_template.render())



# the app configuration section
app = webapp2.WSGIApplication([
    ('/', StartPage),
    ('/createcharacter', CreateCharacterPage),
    ('/gameplay', GameplayPage),
    ('/event1', Event1)
], debug=True)
