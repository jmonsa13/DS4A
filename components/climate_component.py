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
# Function to redirect the type of container to use
def climate_analisis(analisis_type):
    if analisis_type == 'Geo-Type':
        return geo_plot_layout_climate()
    elif analisis_type == 'Time-Series':
        return time_plot_layout_climate()


# Function to change the filter
def climate_analisis_selector(analisis_type):
    if analisis_type == 'Geo-Type':
        return geo_plot_layout_selector_climate()
    elif analisis_type == 'Time-Series':
        return timeseries_layout_selector_climat()

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
# ----------------------------------------------------------------------------------------------------------------------
# Time Series Plot
# ----------------------------------------------------------------------------------------------------------------------
def timeseries_layout_selector_climat():
    layout = [
        dbc.Col(
            [
                html.P("Select a visualization:", style={'font-weight': 'bold'}),
                dcc.RadioItems(id='radio_items_time_climat', options=['World', 'Continents'],
                               value='World',
                               inline=True,
                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                           'margin-left': '20px'})
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
        dbc.Col(
            [
                html.P("Select a format:", style={'font-weight': 'bold'}),
                dcc.RadioItems(id='radio_items_format_climat', options=['Year', 'Month'],
                               value='Year',
                               inline=True,
                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                           'margin-left': '20px'})
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
        dbc.Col(children=[
            html.Br(),
            dcc.RadioItems(id='radio_items_measure_climat', options=['Static', 'Animation'],
                           value='Static',
                           inline=True,
                           labelStyle={'display': 'block', 'cursor': 'pointer',
                                       'margin-left': '20px'})
        ],
            width='auto', style={"margin-left": "10px"},
            id='agg_function_selector_climat'
        ),
        dbc.Col(children=[
            html.Br(),
            dcc.Dropdown(id='year_selection_climat', options=list(range(1960, 2021)),
                           value=[1960, 2020],
                           multi=True)
        ],
            width='auto', style={"margin-left": "10px"},
            id='year_range_climat'
        )
    ]

    return layout

# Time plot layout
def time_plot_layout_climate():
    # Main plot
    layout = [dbc.Col(dcc.Graph(id='Time_plot_climate'), width=12)]
    return layout
