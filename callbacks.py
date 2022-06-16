# Project DS4A - Team 40
# Udjat webApp - Callback function
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import plotly.express as px
from dash import Input, Output
from components.tabs import *


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Variables definition
# ----------------------------------------------------------------------------------------------------------------------
# Path variables

# ----------------------------------------------------------------------------------------------------------------------
# Callback
# ----------------------------------------------------------------------------------------------------------------------
def register_callbacks(app, df, gdf):
    """
    Function that contain all the callback of the app
    :param app: dash app
    :param df: panda dataframe containing the disasters
    :return:
    """

    # callback update_content
    @app.callback(
        Output("app-content", "children"),
        Input("tabs_pages", "value"))
    def update_content(tab):
        return render_content(tab)

    # callback iteraction
    @app.callback(
        Output('Disaster_subgroup', 'figure'),
        Input('subgroup_dropdown', 'value'))
    def update_figure(select_subgroup):
        df_disaster_filter_subgroup = df[df["Disaster Subgroup"] == select_subgroup]

        disasters_by_year_type = df_disaster_filter_subgroup.groupby(by=["Year", "Disaster Type"])[
            "Country"].count().reset_index()

        disasters_by_year_type.columns = ["Year", "Disaster Type", "Count"]

        fig = px.line(disasters_by_year_type, x="Year", y="Count", color='Disaster Type',
                      title=f'# Disasters by Year by {select_subgroup}')
        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"],
                          template='plotly',
                          #plot_bgcolor='rgba(0, 0, 0, 0)',
                          #paper_bgcolor='rgba(0, 0, 0, 0)',
                          )
        return fig

    @app.callback(
        Output('Geo_map', 'figure'),
        Input('radio_items', 'value'),
        Input('disaster_type_dropdown', 'value'))
    def update_figure(selection, disaster_type):
        if disaster_type == 'All':
            df_filter = df.copy()
        else:
            df_filter = df[df["Disaster Subgroup"] == disaster_type]

        if selection == "Countries":
            # Count maps
            disaster_groupby = df_filter.groupby(by=["ISO"]).size().reset_index().rename(
                columns={'ISO': 'Country', 0: 'Count'})

            fig_map = px.choropleth(disaster_groupby, locations="Country",
                                    color="Count",  # number of disasters in each country by year,
                                    color_continuous_scale='Teal',
                                    hover_name="Country",  # column to add to hover information
                                    scope='world',
                                    title="Number of disasters by Country")

            fig_map.update_layout(
                margin=dict(t=50, b=2, l=0, r=0),
                coloraxis_showscale=False,
                geo=dict(
                    showframe=True,
                    showcoastlines=True,
                    projection_type='natural earth'
                ),
                coloraxis_colorbar_x=-0.3,
            )
            return fig_map
        elif selection == "Continents":
            disaster_groupby = df_filter.groupby(by=["Continents"]).size().reset_index().rename(columns={0: 'Count'})

            fig_map = px.choropleth(disaster_groupby,
                                    geojson=gdf.geometry,
                                    locations="Continents",
                                    color="Count",  # number of disasters in each country by year,
                                    color_continuous_scale='Teal',
                                    hover_name="Continents",  # column to add to hover information
                                    scope='world',
                                    title="Number of disasters by Continent")

            fig_map.update_layout(
                margin=dict(t=50, b=5, l=0, r=0),
                coloraxis_showscale=False,
                geo=dict(
                    showframe=True,
                    showcoastlines=True,
                    projection_type='natural earth',
                ),
                coloraxis_colorbar_x=-0.3,
            )

        return fig_map

    @app.callback(
        Output('Time_series', 'figure'),
        Input('Geo_map', 'hoverData'),
        Input('radio_items', 'value'),
        Input('disaster_type_dropdown', 'value'))
    def update_timeseries(hoverData, geo_type, disaster_type):
        # Getting the location
        geo_location = hoverData['points'][0]['location']

        # Filtering by disaster type
        if disaster_type == 'All':
            df_filter = df.copy()
            title = f'All Disasters in {geo_location}'
        else:
            df_filter = df[df["Disaster Subgroup"] == disaster_type]
            title = f'{disaster_type} disasters in {geo_location} '


        if geo_type == "Countries":
            dff = df_filter[df_filter['ISO'] == geo_location]

            disasters_by_year = dff.groupby(by=["Year"]).size().reset_index()
            disasters_by_year.columns = ["Year", "Count"]

        elif geo_type == "Continents":
            dff = df_filter[df_filter['Continents'] == geo_location]

            disasters_by_year = dff.groupby(by=["Year"]).size().reset_index()
            disasters_by_year.columns = ["Year", "Count"]

        fig = px.line(disasters_by_year, x="Year", y="Count", title=title)
        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"])

        return fig
