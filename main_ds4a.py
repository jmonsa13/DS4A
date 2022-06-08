# Project DS4A - Team 40
# Udjat webApp
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import Dash
import dash_bootstrap_components as dbc

from callbacks import register_callbacks
from components.dashboard import *
from components.tabs import *


# ----------------------------------------------------------------------------------------------------------------------
# Main DASH
# ----------------------------------------------------------------------------------------------------------------------
# Run this app with `python main_ds4a.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Defining the object
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY],  # MINTY, SLATE
           meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Title of the app
app.title = 'Udjat 🌎 Team 40 | DS4A'

# Other configuration
# server = app.server
# app.config['suppress_callback_exceptions'] = True

# ----------------------------------------------------------------------------------------------------------------------
# Dash layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                # Logos
                dbc.Col(html.H1([html.Img(src=app.get_asset_url('DS4A.jpg'),
                                          id='logo_ds4a',
                                          style={'height': '40%', 'width': '40%', "margin-left": "20px"},
                                          ),
                                 html.Img(src=app.get_asset_url('Logo_Udjat.PNG'),
                                          id='logo_udjat',
                                          style={'height': '35%', 'width': '35%', "margin-left": "20px"},
                                          )
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Title
                dbc.Col(html.H1(children='Udjat Projet Team 40', style={'textAlign': 'center'}
                                ), width=6
                        ),
                # Tabs
                dbc.Col(html.Div([build_tabs()],
                                 className="one-third column",
                                 id="button",
                                 ), width=4
                        ),
            ],
            id='header', align="center", style={'height': '15%', 'margin-bottom': '40px'}
        ),
        # Content
        html.Div(
            children=dashboard_gui(),
            id='app-content'
        ),
    ],
    id='mainContainer',
    style={'height': '95vh', "display": "flex", "flex-direction": "column"}
)

# Callback
# ----------------------------------------------------------------------------------------------------------------------
register_callbacks(app, df_disaster)

# ----------------------------------------------------------------------------------------------------------------------
# Running the main code
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8050)
    # app.run_server(debug=True, port=8050)
