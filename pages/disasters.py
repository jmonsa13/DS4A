# Project DS4A - Team 40
# Udjat webApp - Disaster page dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.disaster_component import geo_plot_layout
from components.data_component import disaster_subgroup_list


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
                                html.P("Select a type:"),
                                dcc.RadioItems(id='analisis_type', options=['Time-Series', 'Geo-type'],
                                               value='Time-Series',
                                               inline=True,
                                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                                           'margin-left': '20px'})
                            ], width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"}
                        ),

                        dbc.Col(
                            [
                                html.P("Select an option:"),
                                dcc.RadioItems(id='radio_items', options=['Continents', 'Countries'],
                                               value='Continents',
                                               inline=True,
                                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                                           'margin-left': '20px'})
                            ], width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"}
                        ),
                        dbc.Col(
                            [
                                html.P("Select a type of disaster:"),
                                dcc.Dropdown(id='disaster_type_dropdown', options=disaster_subgroup_list,
                                             value=disaster_subgroup_list[-1])
                            ], width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)',
                                               "margin-left": "10px"}
                        )

                    ],
                    style={'height': '80%', "width": "100%", "margin-top": "5px", "margin-left": "5px",
                           "margin-bottom": "20px"},
                    # justify="evenly"
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
