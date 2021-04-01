import dash

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        url_base_pathname='/dash/',
        meta_tags=[meta_viewport]
    )

    dash_app.title = 'Test'

    dash_app.layout = dbc.Container('Hi')

    return dash_app.server