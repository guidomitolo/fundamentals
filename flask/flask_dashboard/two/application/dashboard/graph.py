import dash
from .layout import html_layout

import dash_core_components as dcc
import dash_html_components as html

def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/'
    )

    dash_app.index_string = html_layout

    dash_app.layout = html.Div('Hi')

    return dash_app.server