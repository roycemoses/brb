class UserProf(ndb.Model):
    username = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty()
    choices = ndb.StringProperty(repeated=True)
    #make this a list? ^
