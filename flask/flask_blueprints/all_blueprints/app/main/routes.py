from flask_login import login_required, current_user
from flask import render_template
from app.main import bp

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    return render_template("main/index.html")