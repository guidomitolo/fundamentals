from flask import render_template
from flask_login import login_required

from application.dashboard import bp
from application.dashboard import graph

@bp.route("/dash")
@login_required
def dash_app():
    # the graph is already initialized (only get its url)
    return render_template('dash/dashboard.html', dash_url='/dash/')