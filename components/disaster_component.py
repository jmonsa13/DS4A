# Project DS4A - Team 40
# Udjat webApp - Disaster_component

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc

from components.data_component import *


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------
# Fucntion to redirect the type of container to use
def disaster_analisis(analisis_type):
    if analisis_type == 'Geo-type':
        return geo_plot_layout()
    elif analisis_type == 'Time-Series':
        return time_series_plot_layout()


# Geoplot layout
def geo_plot_layout():
    # Main plot
    layout = [dbc.Col(dcc.Graph(id='Geo_map', hoverData={'points': [{'location': 'North America'}]}), width=6),
              # Second plot
              dbc.Col(dcc.Graph(id='Time_series'), width=6)
              ]
    return layout

# Time_series layout
def time_series_plot_layout():
    # Main plot
    layout = [dbc.Col(dcc.Graph(id='Total_disaster', figure=fig0), width=12)]

    return layout
