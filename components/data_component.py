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

# ISO reading
iso_df = pd.read_excel(data_path + '/ISO_code.xlsx')
iso_dict = dict(zip(iso_df['Code Value'],iso_df['Definition']))
# ----------------------------------------------------------------------------------------------------------------------
# Data Disaster
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

# Replacing the ISO code to name
df_disaster['Countries'] = df_disaster['ISO'].replace(iso_dict)
# ---------------------------------------------------------
# Listing the subgroup of disasters
disaster_subgroup_list = df_disaster["Disaster Subgroup"].unique()
disaster_subgroup_list = np.append(disaster_subgroup_list, 'All')
# ---------------------------------------------------------
# ---------------------------------------------------------
# Reading climate file
# For avoiding the size limitation of github
df_climate_0 = pd.read_csv(data_path + '/Temp_lat_lon_historical_0.csv')
df_climate_1 = pd.read_csv(data_path + '/Temp_lat_lon_historical_1.csv')
df_climate_2 = pd.read_csv(data_path + '/Temp_lat_lon_historical_2.csv')

# Concat
df_climate = pd.concat([df_climate_0, df_climate_1, df_climate_2])
# ----------------------------------------------------------------------------------------------------------------------
# Data Climate
# ----------------------------------------------------------------------------------------------------------------------
# Loading the clean data file as pandas  dataframe
filename_climat = data_path + '/temp_country.csv'
df_climate_country = pd.read_csv(filename_climat)
