# Project DS4A - Team 40
# Udjat webApp - Main Dashboard components dash
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc, Input, Output

import plotly.express as px
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------
# Variables definition
# ----------------------------------------------------------------------------------------------------------------------
# Path variables
image_path = './01_Images'
logo_path = image_path + '/Logo_Udjat.PNG'

data_path = './00_DATA'
raw_data_path = data_path + '/00_RAW_DATA'
clean_data_path = data_path + '/01_CLEAN_DATA'
# ----------------------------------------------------------------------------------------------------------------------
# Data and Plot
# ----------------------------------------------------------------------------------------------------------------------
# Loading the clean data file as pandas  dataframe
filename = clean_data_path + '/Disaster_Clean.xlsx'
df_disaster = pd.read_excel(filename)

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

# ----------------------------------------------------------------------------------------------------------------------
markdown_text = '''
**This text** is using markdown notation the dataset where taken from 
[source dataset](https://www.emdat.be/)
'''

# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------
def dashboard_gui():
    return html.Div(
        [
            html.Br(),

            html.H2(children='Disaster Analysis.'),

            dcc.Markdown(children=markdown_text),

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
        ]
    )
