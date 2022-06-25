# Project DS4A - Team 40
# Udjat webApp - Disaster page dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.disaster_component import geo_plot_layout_selector, geo_plot_layout

# dash-labs plugin call, menu name and route
register_page(__name__, path='/')
# ----------------------------------------------------------------------------------------------------------------------
# Variables definition
# ----------------------------------------------------------------------------------------------------------------------
markdown_text = '''
Disasters generate high human and economic costs which can be mitigated with proper preparation. Understanding 
the effect of external factors such as climate change over natural disasters  is vital to generate strategies 
to diminish such costs. Therefore, we created this visualization tool for analysing the frequency, location, type, 
subtype, and cost of natural disasters covering the period from 1960 and 2021. 
 The data used for this dashboard can be found on [source dataset](https://www.emdat.be/).
'''

# ----------------------------------------------------------------------------------------------------------------------
# Layout for disaster Page
# ----------------------------------------------------------------------------------------------------------------------
layout = dbc.Container(
    html.Div(
        [
            # Title of the pages
            html.H2(children='Disaster Analysis', style={"margin-left": "5px", 'margin-bottom': '20px'}),

            # Content markdown
            dcc.Markdown(children=markdown_text),

            # Selection tools for filtering
            html.Div([
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P("Select a type of analysis:", style={'font-weight': 'bold'}),
                            ], width="auto", style={"margin-left": "10px"}
                        ),
                        dbc.Col(
                            [
                                dcc.Dropdown(options=['Time-Series', 'Geo-type'],
                                             value='Time-Series',
                                             style={'height': '10px'},
                                             id='analisis_type'
                                             )
                            ], width="3",
                        ),
                    ],
                    style={'height': '50%', "width": "100%", "margin-top": "10px", "margin-left": "5px",
                           "margin-bottom": "5px"}
                ),

                # Division line
                dbc.Row(
                    [
                        html.Hr(
                            style={'borderWidth': "5vh", "width": "100%", "borderColor": "#000000", "opacity": "unset"}
                        ),
                    ], style={"margin-left": "5px", "margin-right": "5px"}
                ),

                # Selection tools depending on the initial choice
                dbc.Row(children=geo_plot_layout_selector(),
                        id='disaster-content_selector',
                        style={'height': '80%', "width": "100%", "margin-top": "5px", "margin-left": "5px",
                               "margin-bottom": "20px"},
                        ),

                # Graph plots
                dbc.Row(children=geo_plot_layout(),
                        id='disaster-content',
                        style={'height': '80%', "width": "100%"}
                        ),
            ], style={"border": "1px black solid"}
            ),
        ],
    )
)
