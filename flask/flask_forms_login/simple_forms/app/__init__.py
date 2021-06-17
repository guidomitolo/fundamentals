from flask import Flask
from flask_login import LoginManager
from config import DevConfig

# the core application
app = Flask(__name__, instance_relative_config=False)
app.config.from_object(DevConfig)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
# The message to flash when a user is redirected to the login page.
login_manager.login_message = u"Please login to continue."


from app import routes, models
