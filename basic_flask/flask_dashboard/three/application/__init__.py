from flask import Flask, current_app
from flask_login import LoginManager
from config import DevConfig

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_bootstrap import Bootstrap

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Please login to continue"
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app(config_class=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap.init_app(app)

    with app.app_context():

        login_manager.init_app(app)

        from application import routes, models
            
        db.init_app(app)
        migrate.init_app(app, db)

        from application.auth import bp as auth_bp
        app.register_blueprint(auth_bp)

        # 1. register the dashboard blueprint
        # this is necessary to give the dash a route inside the app
        from application.dashboard import bp as dash_bp
        app.register_blueprint(dash_bp)

        # 2. init the dashboard
        # the dash is initialized within the flask-app context
        from application.dashboard.graph import init_dashboard
        app = init_dashboard(app)

        from application.models import User

        @app.shell_context_processor
        def make_shell_context():
            return {'db': db, 'User': User}

        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id))

        return app