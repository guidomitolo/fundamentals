from flask import Blueprint

bp = Blueprint('dashboard', __name__)

from application.dashboard import routes