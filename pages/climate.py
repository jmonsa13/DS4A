# Project DS4A - Team 40
# Udjat webApp - Climate components dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path='/climate')
# ----------------------------------------------------------------------------------------------------------------------
markdown_text = '''
lalalalal
'''

# ----------------------------------------------------------------------------------------------------------------------
# Layout
# ----------------------------------------------------------------------------------------------------------------------
layout = dbc.Container(
    html.Div(
        [
            html.H2(children='Climate Change Analysis.', style={"margin-left": "5px", 'margin-bottom': '20px'}),

            dcc.Markdown(children=markdown_text),
        ]
    )
)
