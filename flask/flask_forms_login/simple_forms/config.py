import os

basedir = os.path.abspath(os.path.dirname(__file__))

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
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True