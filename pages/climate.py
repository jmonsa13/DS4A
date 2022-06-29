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
Climate change on Earth is one of the main environmental and social problems of humanity due to the consequences 
it can have. Among the main consequences we have: the rise in sea level, the glaciers in the mountains are melting 
and losing surface, thickness, and volume, the ice surface of Greenland and the Arctic is decreasing, rainfall is
 reduced in many places and in elsewhere droughts are worse, extreme weather events are more intense: hurricanes,
  heavy rains, floods, heat waves. Animal and plant species see their habitat displaced or modify their behavior. 

For these reasons, global warming is a challenge that requires the active participation of all agents in society. 
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
