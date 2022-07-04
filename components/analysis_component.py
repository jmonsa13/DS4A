# Project DS4A - Team 40
# Udjat webApp - Analysis_component

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
# Analysis components
# ----------------------------------------------------------------------------------------------------------------------

# Correlation layout selector
def correlation_selector():
    layout = [
        dbc.Col(
            [
                html.P("Select a degree of differencing:", style={'font-weight': 'bold'})
            ], width='auto', style={"margin-left": "10px"}
        ),
        dbc.Col(
            [
                dcc.Dropdown(options=['Zero', 'One diff + log(disaster)'],
                             value='Zero',
                             style={'height': '10px'},
                             id='differencing'
                             )
            ], width=3, style={"margin-left": "2px"}
        ),
        dbc.Col(
            [
                html.P("Select a type of disaster:", style={'font-weight': 'bold'}),
            ], width='auto', style={"margin-left": "5px"}
        ),
        dbc.Col(
            [
                dcc.Dropdown(id='disaster_type_correlation', options=disaster_subgroup_list,
                             value=disaster_subgroup_list[-1])
            ], width=3, style={"margin-left": "2px"}
        ),
    ]

    return layout


# Correlation layout
def correlation_layout():
    # Main plot
    layout = [
        dbc.Col(dcc.Graph(id='Correlation_plot'), width=8),
        # Correlation Values
        dbc.Col(
            [
                html.Br(),
                html.Br(),
                html.H6("Augmented Dickey–Fuller Test Disaster", style={'font-weight': 'bold'}),
                html.P(style={'font-weight': 'bold'}, id='adf_test_disaster'),
                html.P(style={'font-weight': 'bold'}, id='stationary_disaster'),
                html.Br(),
                html.H6("Augmented Dickey–Fuller Test Climate", style={'font-weight': 'bold'}),
                html.P(style={'font-weight': 'bold'}, id='adf_test_climate'),
                html.P(style={'font-weight': 'bold'}, id='stationary_climate'),
                html.Br(),
                html.H4(id='correlation_message', style={'font-weight': 'bold'}),

            ], width='auto', style={"margin-left": "10px"}

        )
    ]
    return layout

# Correlation layout selector
def arima_selector():
    layout = [
        dbc.Col(
            [
                html.P("Select a time series:", style={'font-weight': 'bold'})
            ], width='auto', style={"margin-left": "10px"}
        ),
        dbc.Col(
            [
                dcc.Dropdown(options=['Disasters', 'World Temperature'],
                             value='Disasters',
                             style={'height': '10px'},
                             id='Arima_select'
                             )
            ], width=3, style={"margin-left": "2px"}
        ),
    ]

    return layout

# Correlation layout
def arima_layout():
    # Main plot
    layout = [
        dbc.Col(dcc.Graph(id='Arima_plot'), width=12),
    ]
    return layout
