# Project DS4A - Team 40
# Udjat webApp - Climate page dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.climate_component import geo_plot_layout_selector_climate, geo_plot_layout_climate


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
            # Title of the pages
            html.H2(children='Climate Change Analysis', style={"margin-left": "5px", 'margin-bottom': '20px'}),

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
                                dcc.Dropdown(options=['Time-Series', 'Geo-Type'],
                                             value='Geo-Type',
                                             style={'height': '10px'},
                                             id='analisis_type_Climat'
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
                dbc.Row(children=geo_plot_layout_selector_climate(),
                        id='climate-content_selector',
                        style={'height': '80%', "width": "100%", "margin-top": "5px", "margin-left": "5px",
                               "margin-bottom": "20px"},
                        ),

                # Graph plots
                dbc.Row(children=geo_plot_layout_climate(),
                        id='climate-content',
                        style={'height': '80%', "width": "100%"}
                        ),

            ], style={"border": "1px black solid"}
            )
        ]
    )
)
