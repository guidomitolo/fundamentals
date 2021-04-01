from flask import render_template
from flask_login import login_required

from application.dashboard import bp
from application.dashboard import graph

@bp.route("/dash_app")
@login_required
def dash_app():
    return render_template('dashboard/dash_app.html', dash_url=graph.URL_BASE, min_height=graph.MIN_HEIGHT)