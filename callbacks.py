# Project DS4A - Team 40
# Udjat webApp - Callback function

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import plotly.express as px
from dash import Input, Output

from components.disaster_component import disaster_analisis_selector, disaster_analisis


# ----------------------------------------------------------------------------------------------------------------------
# Callback
# ----------------------------------------------------------------------------------------------------------------------
# Main callback situation
def register_callbacks(app, df, gdf):
    """
    Function that contain all the callback of the app
    :param app: dash app
    :param df: panda dataframe containing the disasters
    :param gdf: Geo dataframe containing the Continent
    :return:
    """

# ----------------------------------------------------------------------------------------------------------------------
# Callback for changing the type of analisis (Time-series or Geoplot)
    @app.callback(
        Output('disaster-content', 'children'),
        Input('analisis_type', 'value'))
    def geo_timeseries_content(analisis_type):
        return disaster_analisis(analisis_type)

# ----------------------------------------------------------------------------------------------------------------------
# Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('disaster-content_selector', 'children'),
        Input('analisis_type', 'value'))
    def geo_timeseries_selector(analisis_type):
        return disaster_analisis_selector(analisis_type)

    # ----------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('agg_function_selector', 'style'),
        Input('radio_items_format', 'value'))
    def timeseries_aggfunction_selector(selection):
        if selection == 'Frequency':
            return {'display': 'None'}
        if selection == 'Economical Impact':
            return {'display': 'block'}

    # ----------------------------------------------------------------------------------------------------------------------
    # callback iteraction
    @app.callback(
        Output('Total_disaster', 'figure'),
        Input('radio_items_time', 'value'),
        Input('radio_items_format', 'value'),
        Input('radio_items_measure', 'value'))
    def update_figure_time(select_type, select_format, agg_type='Sum'):
        # filtering by type of disaster
        if select_type == 'All disasters':
            if select_format == 'Frequency':
                disasters_by_year = df["Year"].value_counts().to_frame().reset_index()
                disasters_by_year.columns = ["Year", "Count"]
                disasters_by_year = disasters_by_year.sort_values(by="Year", ascending=False)

                # Plotly
                fig = px.line(disasters_by_year, x="Year", y="Count", title='Total Disasters by Year')

            elif select_format == 'Economical Impact':
                # Sum total cost
                if agg_type == 'Sum':
                    total_damage_sum_year = df.groupby(by="Year")["Total Damages, Adjusted ('000 US$)"]\
                        .sum().reset_index()
                    total_damage_sum_year.columns = ["Year", "Total Damages, Adjusted ('000 US$) SUM"]

                    # Plotly
                    fig = px.bar(total_damage_sum_year, x="Year", y="Total Damages, Adjusted ('000 US$) SUM",
                                 title='Total Cost of Disasters by Year')

                # Average total cost by year
                elif agg_type == 'Mean':
                    total_damage_sum_year = df.groupby(by="Year")["Total Damages, Adjusted ('000 US$)"]\
                        .mean().reset_index()
                    total_damage_sum_year.columns = ["Year", "Total Damages, Adjusted ('000 US$) MEAN"]

                    # Plotly
                    fig = px.bar(total_damage_sum_year, x="Year", y="Total Damages, Adjusted ('000 US$) MEAN",
                                 title='Mean Cost of Disasters by Year')

        elif select_type == 'By type':
            if select_format == 'Frequency':
                # Disaster by subgroup
                disasters_by_year_subgroup = df.groupby(by=["Year", "Disaster Subgroup"]).size().reset_index()
                disasters_by_year_subgroup.columns = ["Year", "Disaster Type", "Count"]

                # plotly
                fig = px.line(disasters_by_year_subgroup, x="Year", y="Count", color='Disaster Type',
                              title='Total Disasters by Year for every Disaster Type')

            elif select_format == 'Economical Impact':
                # Sum total cost

                if agg_type == 'Sum':
                    total_damage_sum_year = df.groupby(by=["Year"
                        , "Disaster Subgroup"])["Total Damages, Adjusted ('000 US$)"].sum().reset_index()
                    total_damage_sum_year.columns = ["Year", "Disaster Type", "Total Damages, Adjusted ('000 US$) SUM"]

                    # Plotly
                    fig = px.bar(total_damage_sum_year, x="Year", y="Total Damages, Adjusted ('000 US$) SUM",
                                 color="Disaster Type", title='Total Cost of Disasters by Year and Type')

                # Average total cost by year
                elif agg_type == 'Mean':
                    total_damage_sum_year = df.groupby(by=["Year"
                        , "Disaster Subgroup"])["Total Damages, Adjusted ('000 US$)"].mean().reset_index()
                    total_damage_sum_year.columns = ["Year", "Disaster Type", "Total Damages, Adjusted ('000 US$) MEAN"]

                    # Plotly
                    fig = px.bar(total_damage_sum_year, x="Year", y="Total Damages, Adjusted ('000 US$) MEAN",
                                 color="Disaster Type", title='Mean Cost of Disasters by Year and Type')

        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"], template='seaborn')

        return fig

# ----------------------------------------------------------------------------------------------------------------------
# Callback for updating the geoplot of disasters
    @app.callback(
        Output('Geo_map', 'figure'),
        Input('radio_items', 'value'),
        Input('disaster_type_dropdown', 'value'),
        Input('geo_items_format', 'value'))
    def update_figure(selection, disaster_type, format):
        # filtering by type of disasters
        if disaster_type == 'All':
            df_filter = df.copy()
        else:
            df_filter = df[df["Disaster Subgroup"] == disaster_type]

        # Filtering by countries
        if selection == "Countries":

            # Filtering by Format
            if format == 'Frequency':
                # Count by countries
                disaster_groupby = df_filter.groupby(by=["ISO", 'Countries']).size().reset_index().rename(
                    columns={'ISO': 'Country', 0: 'Count'})

                # Geo map
                fig_map = px.choropleth(disaster_groupby, locations="Country",
                                        color="Count",  # number of disasters in each country by year,
                                        color_continuous_scale='Teal',
                                        hover_name="Countries",  # column to add to hover information
                                        scope='world',
                                        title="Number of Disasters by Country")

            elif format == 'Economical Impact':
                # Sum by countries
                disaster_groupby = df_filter.groupby(by=["ISO", 'Countries'])["Total Damages, Adjusted ('000 US$)"].\
                    sum().reset_index().rename(columns={'ISO': 'Country'})

                # Geo map
                fig_map = px.choropleth(disaster_groupby, locations="Country",
                                        color="Total Damages, Adjusted ('000 US$)",
                                        color_continuous_scale='Teal',
                                        hover_name='Countries',  # column to add to hover information
                                        scope='world',
                                        title="Total Damage (USD) of Disasters by Country")

        # Filtering by continents
        elif selection == "Continents":
            # Filtering by Format
            if format == 'Frequency':
                # Count by continents
                disaster_groupby = df_filter.groupby(by=["Continents"]).size()\
                    .reset_index().rename(columns={0: 'Count'})

                # Geo map
                fig_map = px.choropleth(disaster_groupby,
                                        geojson=gdf.geometry,
                                        locations="Continents",
                                        color="Count",  # number of disasters in each country by year,
                                        color_continuous_scale='Teal',
                                        hover_name="Continents",  # column to add to hover information
                                        scope='world',
                                        title="Number of Disasters by Continent")

            elif format == 'Economical Impact':
                # Sum by continents
                disaster_groupby = df_filter.groupby(by=["Continents"])["Total Damages, Adjusted ('000 US$)"].\
                    sum().reset_index()

                # Geo map
                fig_map = px.choropleth(disaster_groupby,
                                        geojson=gdf.geometry,
                                        locations="Continents",
                                        color="Total Damages, Adjusted ('000 US$)",
                                        color_continuous_scale='Teal',
                                        hover_name="Continents",  # column to add to hover information
                                        scope='world',
                                        title="Total Damage (USD) of Disasters by Continent")

        # Update layout of map
        fig_map.update_layout(
            margin=dict(t=50, b=2, l=0, r=0),
            coloraxis_showscale=False,
            geo=dict(
                showframe=True,
                showcoastlines=True,
                projection_type='natural earth',
            ),
            coloraxis_colorbar_x=-0.3,
        )

        return fig_map

# ----------------------------------------------------------------------------------------------------------------------
# Callback for updating the time series of the geo map.
    @app.callback(
        Output('Time_series', 'figure'),
        Input('Geo_map', 'hoverData'),
        Input('radio_items', 'value'),
        Input('disaster_type_dropdown', 'value'),
        Input('geo_items_format', 'value'))
    def update_timeseries(hoverData, geo_type, disaster_type, format):
        # Getting the location
        geo_location = hoverData['points'][0]['location']

        # Filtering by disaster type
        if disaster_type == 'All':
            df_filter = df.copy()
            title = f'All Disasters in'
        else:
            df_filter = df[df["Disaster Subgroup"] == disaster_type]
            title = f'{disaster_type} Disasters in'

        # Filtering by countries or continents
        if geo_type == "Countries":
            dff = df_filter[df_filter['ISO'] == geo_location]

            country = dff.iloc[0]['Countries']
            title = title + f' {country}'

        elif geo_type == "Continents":
            dff = df_filter[df_filter['Continents'] == geo_location]
            title = title + f' {geo_location}'

        # Filtering by Format
        if format == 'Frequency':
            disasters_by_year = dff.groupby(by=["Year"]).size().reset_index()
            disasters_by_year.columns = ["Year", "Count"]

            # Empty df for year range
            min_year = int(disasters_by_year['Year'].min())
            empty_df = pd.DataFrame(data=range(min_year, 2022), columns=['Year'])

            # filling the empty years
            disasters_by_year_complete = pd.merge(left=disasters_by_year, right=empty_df, on='Year', how='right')
            disasters_by_year_complete.fillna(0, inplace=True)

            fig = px.line(disasters_by_year_complete, x="Year", y="Count", title=title)
        elif format == 'Economical Impact':
            title = title + ' by Economical Impact'
            disasters_by_economical = dff.groupby(by=["Year"])["Total Damages, Adjusted ('000 US$)"].sum().reset_index()
            disasters_by_economical.columns = ["Year", "Total Damages, Adjusted ('000 US$) SUM"]

            fig = px.line(disasters_by_economical, x="Year", y="Total Damages, Adjusted ('000 US$) SUM", title=title)

        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"])

        return fig
