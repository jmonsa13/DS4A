# Project DS4A - Team 40
# Udjat webApp
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Variables definition
# ----------------------------------------------------------------------------------------------------------------------
# Path variables
data_path = './00_DATA'
raw_data_path = data_path + '/00_RAW_DATA'
clean_data_path = data_path + '/01_CLEAN_DATA'
# ----------------------------------------------------------------------------------------------------------------------
# Main CODE
# ----------------------------------------------------------------------------------------------------------------------
# Loading the clean data file as pandas  dataframe
filename = clean_data_path + '/Disaster_Clean.xlsx'
df_disaster = pd.read_excel(filename)


disaster_groupby = df_disaster.groupby(by=["ISO"]).size().reset_index().rename(columns={'ISO': 'Country', 0: 'Count'})

fig = px.choropleth(disaster_groupby, locations="Country",
                    color="Count", # number of disasters in each country by year,
                    color_continuous_scale="Viridis",
                    hover_name="Country", # column to add to hover information
                    title="Number of disasters by Country")
# ----------------------------------------------------------------------------------------------------------------------
# Main DASH
# ----------------------------------------------------------------------------------------------------------------------
# Run this app with `python Main_DS4A.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# Defining the object
app = Dash(__name__)

# Dash layout
app.layout = html.Div(children=[
    html.H1(children='Udjat Projet Team 40'),

    html.Div(children='''
        Front end DRAFT.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Running the main code
if __name__ == '__main__':
    app.run_server(debug=True)
