# Project DS4A - Team 40
# Udjat webApp - Analysis page dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.analysis_component import correlation_selector, correlation_layout, arima_selector, arima_layout

# dash-labs plugin call, menu name and route
register_page(__name__, path='/analysis')
# ----------------------------------------------------------------------------------------------------------------------
# Variables definition
# ----------------------------------------------------------------------------------------------------------------------
markdown_text = '''
Let's analysis the following hypothesis. **Is climate change increasing the  frequency of natural disasters?**
'''
correlation_markdown = '''
Let's correlate the frequency of disaster vs the world temperature. So we can answer the question:
**Is temperature related to the presentation of natural disasters?** In this case we are facing two variables
 (number of disasters and average of temperature) measured over time. To find the correlation between two time series, 
 the cross-correlation technique can be used. The proper use of the cross-correlation technique requires
  **stationarity** in the series, as a prior and mandatory condition. Therefore, we have to difference the series until 
  achieving this.
'''

arima_markdown = '''
Let's use traditional time series forecast methods to predict how the frequency of disasters and the average 
temperature around the world will behave in the future, for this we can use the **ARIMA method**. In order to apply 
ARIMA correctly, the time series have to be stationary. Therefore, we need to difference both data sets one time.
'''
# ----------------------------------------------------------------------------------------------------------------------
# Layout for disaster Page
# ----------------------------------------------------------------------------------------------------------------------
layout = dbc.Container(
    html.Div(
        [
            # Title of the pages
            html.H2(children='General Analysis', style={"margin-left": "5px", 'margin-bottom': '20px'}),

            # Content markdown
            dcc.Markdown(children=markdown_text),

            # Correlation
            html.Div([
                dbc.Row(
                    [
                        # Subtitle
                        html.H5(children='Correlation', style={"margin-left": "10px", 'margin-bottom': '20px',
                                                               "margin-top": "10px"}),

                        # Content markdown
                        dcc.Markdown(children=correlation_markdown, style={"margin-left": "10px"}),

                    ]
                ),
                # Selections
                dbc.Row(
                    children=correlation_selector(),
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

                # Graph plots
                dbc.Row(children=correlation_layout(),
                        id='correlation_content',
                        style={'height': '80%', "width": "100%"}
                        ),
            ], style={"border": "1px black solid"}
            ),
            # Space
            html.Br(),
            # Arima
            html.Div([
                dbc.Row(
                    [
                        # Subtitle
                        html.H5(children='ARIMA', style={"margin-left": "10px", 'margin-bottom': '20px',
                                                         "margin-top": "10px"}),

                        # Content markdown
                        dcc.Markdown(children=arima_markdown, style={"margin-left": "10px"}),

                    ]
                ),
                # Selections
                dbc.Row(
                    children=arima_selector(),
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

                # Graph plots
                dbc.Row(children=arima_layout(),
                        id='arima_content',
                        style={'height': '80%', "width": "100%"}
                        ),
            ], style={"border": "1px black solid"}
            ),

        ],
    )
)
