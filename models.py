from google.appengine.ext import ndb

class Profile(ndb.Model):
    nickname = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty()
    joined_on = ndb.DateTimeProperty(auto_now_add=True)
    updated_on = ndb.DateTimeProperty(auto_now=True)



    # username = ndb.StringProperty(required=True)
    # user_id = ndb.StringProperty()
    # choices = ndb.StringProperty(repeated=True)
    #make this a list? ^
