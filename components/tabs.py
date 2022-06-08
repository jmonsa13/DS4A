# Project DS4A - Team 40
# Udjat webApp - tabs components dash
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
from components.dashboard import *


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------
def build_tabs():
    return dcc.Tabs(id="tabs_pages", value='Dashboard', children=[
                    dcc.Tab(label='Dashboard', value='Dashboard'),
                    dcc.Tab(label='Simulation', value='Simulation'),
                    dcc.Tab(label='About Us', value='About')
                    ], colors={"border": "white", "primary": "white", "background": "Gainsboro"}
                    )


# ----------------------------------------------------------------------------------------------------------------------
# Callback
# ----------------------------------------------------------------------------------------------------------------------
def render_content(tab):
    if tab == 'Dashboard':
        return dashboard_gui()
    elif tab == 'Simulation':
        return html.Div([
            html.H2('Simulation'),
            html.Br(),
            html.P('This site is under construction, came back later')
        ])
    elif tab == 'About':
        return html.Div([
            html.H2('About Team 40'),
            html.Br(),
            html.P('This site is under construction, came back later')
        ])
