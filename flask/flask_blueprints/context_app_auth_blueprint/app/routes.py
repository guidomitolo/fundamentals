from flask_login import login_required, current_user
from flask import render_template

# thanks to the context handler the login manager is imported
from app import current_app as app

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html")