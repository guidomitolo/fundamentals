from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, user_id, username, email, password, active=True):

        self.id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.active = active

    def __repr__(self):
        return self.username