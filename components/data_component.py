# Project DS4A - Team 40
# Udjat webApp - Data_component

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
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