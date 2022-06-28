# Project DS4A - Team 40
# Udjat webApp - Climate component

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc

from components.data_component import *


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Geo_plot
# ----------------------------------------------------------------------------------------------------------------------
# Geoplot layout selector
def geo_plot_layout_selector_climate():
    layout = [
        dbc.Col(
            [
                html.P("Select a Year:", style={'font-weight': 'bold'}),
                dcc.Slider(min=1960, max=2020, step=1, value=1960, id='year_climat',
                           marks={i: f'{int(i)}' for i in range(1960, 2022, 5)},
                           tooltip={'always_visible': True, 'placement': 'bottom'}),
            ],
            width=8, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
        dbc.Col(
            [
                html.P("Select a Format:", style={'font-weight': 'bold'}),
                dcc.RadioItems(id='radio_climat', options=['Absolute', 'Relative'],
                               value='Absolute',
                               inline=True,
                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                           'margin-left': '5px'})
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "5px"},
        ),
    ]

    return layout


# Geoplot layout
def geo_plot_layout_climate():
    # Main plot
    layout = [dbc.Col(dcc.Graph(id='Geo_map_climate'), width=8),
              dbc.Col([
                  html.Br(),
                  html.Br(),
                  dbc.Row([html.H5('Maximum Temperature',  style={'font-weight': 'bold'}),
                           html.P(style={'font-weight': 'bold'}, id='Max_temp_climat'),
                           ]),
                  html.Br(),
                  dbc.Row([html.H5('Minimum Temperature',  style={'font-weight': 'bold'}),
                           html.P(style={'font-weight': 'bold'}, id='Min_temp_climat'),
                           ]),
                  html.Br(),
                  dbc.Row([html.H5('Average Temperature',  style={'font-weight': 'bold'}),
                           html.P(style={'font-weight': 'bold'}, id='Average_temp_climat'),
                           ]),
              ], width=3)
              ]
    return layout
