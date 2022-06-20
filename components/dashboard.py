# Project DS4A - Team 40
# Udjat webApp - Main Dashboard components dash
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px

import numpy as np
import pandas as pd
import geopandas as gpd
import json

# ----------------------------------------------------------------------------------------------------------------------
# Variables definition
# ----------------------------------------------------------------------------------------------------------------------
# Path variables
data_path = './data'

# Continent json maps
# Opening JSON file
f = open(data_path + '/continent.json')
cont = json.load(f)

gdf = gpd.GeoDataFrame.from_features(cont)
gdf = gdf.set_index("CONTINENT")
# ----------------------------------------------------------------------------------------------------------------------
# Data and Plot
# ----------------------------------------------------------------------------------------------------------------------
# Loading the clean data file as pandas  dataframe
filename = data_path + '/Disaster_Clean.xlsx'
df_disaster = pd.read_excel(filename)
# ---------------------------------------------------------
# Creating the continent columns
new_continent = []
for index, row in df_disaster.iterrows():
    if row['Continent'] == "Americas":
        new_continent.append(row["Region"])
    elif row['ISO'] == "AUS":
        new_continent.append('Australia')
    else:
        new_continent.append(row["Continent"])

# Creating the new column
df_disaster["Continents"] = new_continent
df_disaster["Continents"].replace({"Northern America": "North America", "Caribbean": "South America",
                                   "Central America": "North America"}, inplace=True)

# ---------------------------------------------------------
# Disaster by subgroup
# Checking how many records we have per year
disasters_by_year_subgroup = df_disaster.groupby(by=["Year", "Disaster Subgroup"]).size().reset_index()
disasters_by_year_subgroup.columns = ["Year", "Disaster Subgroup", "Count"]

fig0 = px.line(disasters_by_year_subgroup, x="Year", y="Count", color='Disaster Subgroup', title='# Disasters by Year')
fig0.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"])

# ---------------------------------------------------------
# Listing the subgroup of disasters
disaster_subgroup_list = df_disaster["Disaster Subgroup"].unique()
disaster_subgroup_list = np.append(disaster_subgroup_list, 'All')

# ----------------------------------------------------------------------------------------------------------------------
markdown_text = '''
Visualization of the frequency and location of natural disasters.
[source dataset](https://www.emdat.be/)
'''


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------
def dashboard_gui():
    return html.Div(
        [
            html.H2(children='Disaster Analysis.', style={"margin-left": "5px", 'margin-bottom': '20px'}),

            dcc.Markdown(children=markdown_text),

            html.Div([
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.P("Select a type:"),
                            dcc.RadioItems(id='analisis_type', options=['Time-Series', 'Geo-type'], value='Continents',
                                           inline=True,
                                           labelStyle={'display': 'block', 'cursor': 'pointer', 'margin-left': '20px'})
                        ], width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"}
                    ),

                    dbc.Col(
                        [
                            html.P("Select an option:"),
                            dcc.RadioItems(id='radio_items', options=['Continents', 'Countries'], value='Continents',
                                           inline=True,
                                           labelStyle={'display': 'block', 'cursor': 'pointer', 'margin-left': '20px'})
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
                #justify="evenly"
            ),

            dbc.Row(
                [
                    # Main plot
                    dbc.Col(dcc.Graph(id='Geo_map',
                                      hoverData={'points': [{'location': 'North America'}]}), width=6
                            ),
                    # Second plot
                    dbc.Col(dcc.Graph(id='Time_series'), width=6
                            ),

                ],
                style={'height': '80%', "width": "100%"}
            ),
            ], style={"border": "1px black solid"}
            ),



            html.H3(children='Total disaster'),
            dcc.Graph(
                id='Total_disaster',
                figure=fig0
            ),

            html.H4(children='Disaster by subgroup'),

            html.Div(children=[
                html.Label('Dropdown'),
                dcc.Dropdown(id='subgroup_dropdown', options=disaster_subgroup_list,
                             value=disaster_subgroup_list[0])
            ]
            ),
            dcc.Graph(id='Disaster_subgroup')
        ],
    )
