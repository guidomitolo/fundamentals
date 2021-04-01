import os
# let load local stored env variables
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Base config."""
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    # protect web forms against Cross-Site Request Forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevConfig(Config):
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = os.environ.get('DEBUG')
    TESTING = True