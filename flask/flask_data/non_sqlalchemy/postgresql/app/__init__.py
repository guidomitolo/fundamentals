from flask import Flask, current_app
from flask_login import LoginManager
from config import DevConfig

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Please login to continue."

def create_app(config_class=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():

        login_manager.init_app(app)

        from . import routes, models, database

        database.init_app(app)

        from app.auth import bp as auth_bp
        app.register_blueprint(auth_bp)

        return app
