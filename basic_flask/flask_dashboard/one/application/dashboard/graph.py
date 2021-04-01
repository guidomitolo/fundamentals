import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from application.dashboard import _protect_dashviews

APP_ID = 'dash_app'
URL_BASE = '/dashboard/dash_app/'
MIN_HEIGHT = 200

def add_dash(server, login_reg=True):

    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
    ]

    app = dash.Dash(
        server=server,
        url_base_pathname=URL_BASE,
        suppress_callback_exceptions=True,
        external_stylesheets=external_stylesheets
    )

    app.layout = dbc.Container([
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(["Input: ",
                  dcc.Input(id=f'{APP_ID}_my_input', value='initial value', type='text')]),
        html.Br(),
        html.Div(id=f'{APP_ID}_my_output'),

    ])

    @app.callback(
        Output(component_id=f'{APP_ID}_my_output', component_property='children'),
        [Input(component_id=f'{APP_ID}_my_input', component_property='value')]
    )
    def update_output_div(input_value):
        return 'Output: {}'.format(input_value)

    if login_reg:
        _protect_dashviews(app)

    return server