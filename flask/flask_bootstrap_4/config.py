
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    # signal the application every time a change is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('DEBUG')
    TESTING = True