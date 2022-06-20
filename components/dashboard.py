# Project DS4A - Team 40
# Udjat webApp - Main Dashboard components dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
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
