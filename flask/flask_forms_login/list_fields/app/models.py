from flask_login import UserMixin

# a user object which represents the properties for the users
class User(UserMixin):
    def __init__(self , username , password , num , active=True):

        # avoid naming "id" the constructor parameter

        self.id = num
        self.username = username
        self.password = password
        self.active = active

    # these methods can be inherited from UserMixin as attributes:

    # def get_id(self):
    #     return self.id

    # This one must return a unicode that uniquely identifies this user, 
    # and can be used to load the user from the user_loader callback. 
    # Note that this must be a unicode - if the ID is natively an int or some other type, 
    # you will need to convert it to unicode.

    # def is_active(self):
    #     return self.active

# temporal registered users repository
class UsersRepo():

    def __init__(self):
        self.users = dict()
        self.users_id_dict = dict()
        self.identifier = 0
    
    def save_user(self, user):
        # save User object in dict
        self.users_id_dict[user.id] = user
        self.users[user.username] = user
    
    def get_user_by_name(self, username):
        # the dict method "get()" returns None if no key
        return self.users.get(username)
    
    def get_user_by_id(self, userid):
        return self.users_id_dict.get(userid)
    
    def next_index(self):
        self.identifier +=1
        return self.identifier