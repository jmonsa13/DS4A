# Project DS4A - Team 40
# Udjat webApp - tabs components dash
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc

from components.dashboard import *
from components.about import *


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------
def build_tabs():
    tab_height = '6vh'

    return dcc.Tabs(id="tabs_pages", value='Dashboard', children=[
                    dcc.Tab(label='Dashboard', value='Dashboard',
                            style={'padding': '0', 'line-height': tab_height},
                            selected_style={'padding': '0', 'line-height': tab_height}),
                    dcc.Tab(label='Simulation', value='Simulation',
                            style={'padding': '0', 'line-height': tab_height},
                            selected_style={'padding': '0', 'line-height': tab_height}),
                    dcc.Tab(label='About Us', value='About',
                            style={'padding': '0', 'line-height': tab_height},
                            selected_style={'padding': '0', 'line-height': tab_height})
                    ], colors={"border": "white", "primary": "white", "background": "Gainsboro"},
                    style={
                        'width': '100%',
                        'font-size': '90%',
                        'height': tab_height}
                    )


# ----------------------------------------------------------------------------------------------------------------------
def render_content(tab):
    if tab == 'Dashboard':
        return dashboard_gui()
    elif tab == 'Simulation':
        return html.Div([
            html.H2('Simulation', style={"margin-left": "5px", 'margin-bottom': '20px'}),
            html.P('This site is under construction, came back later')
        ])
    elif tab == 'About':
        return about_gui()
