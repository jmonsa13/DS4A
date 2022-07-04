# Project DS4A - Team 40
# Udjat webApp - Callback function

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import Input, Output

from statsmodels.tsa import stattools
from statsmodels.tsa.arima.model import ARIMA

from components.disaster_component import disaster_analisis_selector, disaster_analisis
from components.climate_component import climate_analisis, climate_analisis_selector


# ----------------------------------------------------------------------------------------------------------------------
# Callback
# ----------------------------------------------------------------------------------------------------------------------
# Main callback situation
def register_callbacks(app, df, gdf, df_climate, df_climate_country):
    """
    Function that contain all the callback of the app
    :param app: dash app
    :param df: panda dataframe containing the disasters
    :param gdf: Geo dataframe containing the Continent
    :param df_climate: Temperature by year and lat & lon
    :param df_climate_country: Temperature by year, month in every countries
    :return:
    """

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of analisis (Time-series or Geoplot)
    @app.callback(
        Output('disaster-content', 'children'),
        Input('analisis_type', 'value'))
    def geo_timeseries_content(analisis_type):
        return disaster_analisis(analisis_type)

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('disaster-content_selector', 'children'),
        Input('analisis_type', 'value'))
    def geo_timeseries_selector(analisis_type):
        return disaster_analisis_selector(analisis_type)

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('agg_function_selector', 'style'),
        Input('radio_items_format', 'value'))
    def timeseries_aggfunction_selector(selection):
        if selection == 'Frequency':
            return {'display': 'None'}
        if selection == 'Economical Impact':
            return {'display': 'block'}

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('agg_function_selector_climat', 'style'),
        Input('radio_items_format_climat', 'value'))
    def timeseries_aggfunction_selector_climat(selection):
        if selection == 'Year':
            return {'display': 'None'}
        if selection == 'Month':
            return {'display': 'block'}

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('year_range_climat', 'style'),
        Input('radio_items_time_climat', 'value'),
        Input('radio_items_measure_climat', 'value'),
        Input('radio_items_format_climat', 'value'))
    def timeseries_aggfunction_selector_climat_static(visual, selection, formato):
        if visual == 'Continents' or formato == 'Year':
            return {'display': 'None'}
        elif formato == 'Month':
            if selection == 'Animation':
                return {'display': 'None'}
            if selection == 'Static':
                return {'display': 'block'}

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of analisis (Time-series or Geoplot)
    @app.callback(
        Output('climate-content', 'children'),
        Input('analisis_type_Climat', 'value'))
    def geo_timeseries_content_climat(analisis_type):
        return climate_analisis(analisis_type)

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for changing the type of filter (Time-series or Geoplot)
    @app.callback(
        Output('climate-content_selector', 'children'),
        Input('analisis_type_Climat', 'value'))
    def geo_timeseries_selector(analisis_type):
        return climate_analisis_selector(analisis_type)

    # ------------------------------------------------------------------------------------------------------------------
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
                    total_damage_sum_year = df.groupby(by="Year")["Total Damages, Adjusted ('000 US$)"] \
                        .sum().reset_index()
                    total_damage_sum_year.columns = ["Year", "Total Damages, Adjusted ('000 US$) SUM"]

                    # Plotly
                    fig = px.bar(total_damage_sum_year, x="Year", y="Total Damages, Adjusted ('000 US$) SUM",
                                 title='Total Cost of Disasters by Year')

                # Average total cost by year
                elif agg_type == 'Mean':
                    total_damage_sum_year = df.groupby(by="Year")["Total Damages, Adjusted ('000 US$)"] \
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

    # ------------------------------------------------------------------------------------------------------------------
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
                disaster_groupby = df_filter.groupby(by=["ISO", 'Countries'])["Total Damages, Adjusted ('000 US$)"]. \
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
                disaster_groupby = df_filter.groupby(by=["Continents"]).size() \
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
                disaster_groupby = df_filter.groupby(by=["Continents"])["Total Damages, Adjusted ('000 US$)"]. \
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

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
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

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for updating the time series of the geo map.
    @app.callback(
        Output('Geo_map_climate', 'figure'),
        Input('year_climat', 'value'),
        Input('radio_climat', 'value'))
    def update_climate_year_geo(year, formato):
        if formato == 'Absolute':
            # Filter year
            df_filter = df_climate[df_climate['year'] == year].copy()

            # Title
            title = f'Average Temperature of the World in {year}'

            # Configuration
            marker_conf = dict(
                size=3,
                color=np.round(df_filter["timeseries-tas-annual-mean"], 2),  # set color equal to a variable
                colorscale='Thermal',  # one of plotly colorscales,
                showscale=True,
                colorbar=dict(title='Temperature °C'))

        elif formato == 'Relative':
            # Baseline year 1960
            df_filter_1960 = df_climate[df_climate['year'] == 1960].copy()

            # Filter year
            df_filter = df_climate[df_climate['year'] == year].copy()

            # Relative value
            df_filter['timeseries-tas-annual-mean'] = df_filter['timeseries-tas-annual-mean'].values \
                                                      - df_filter_1960['timeseries-tas-annual-mean'].values

            # Title
            title = f'Relative Change of Temperature on the World in {year} Compared to 1960'

            # Configuration
            marker_conf = dict(
                size=3,
                color=np.round(df_filter["timeseries-tas-annual-mean"], 2),  # set color equal to a variable
                colorscale='Thermal',  # one of plotly colorscales,
                showscale=True,
                cmax=4,
                cmin=-1,
                colorbar=dict(title='Temperature °C'))

        # Plotly
        fig = go.Figure(data=go.Scattergeo(
            lon=df_filter['lon_bnds'],
            lat=df_filter['lat_bnds'],
            text=np.round(df_filter["timeseries-tas-annual-mean"], 2),
            mode='markers',
            marker=marker_conf))

        # Update layout of map
        fig.update_layout(title=title)

        # Update layout of map
        fig.update_layout(
            margin=dict(t=50, b=2, l=0, r=0),
            coloraxis_showscale=False,
            geo=dict(
                showframe=True,
                showcoastlines=True,
                projection_type='natural earth',
            ),
            coloraxis_colorbar_x=-0.3,
        )

        return fig

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for updating the time series of the geo map.
    @app.callback(
        [Output('Max_temp_climat', 'children'),
         Output('Min_temp_climat', 'children'),
         Output('Average_temp_climat', 'children')],
        [Input('year_climat', 'value'),
         Input('radio_climat', 'value')]
    )
    def update_climate_year(year, formato):
        if formato == 'Absolute':
            # Filter year
            df_filter = df_climate[df_climate['year'] == year]

        elif formato == 'Relative':
            # Baseline year 1960
            df_filter_1960 = df_climate[df_climate['year'] == 1960].copy()

            # Filter year
            df_filter = df_climate[df_climate['year'] == year].copy()

            # Relative value
            df_filter['timeseries-tas-annual-mean'] = df_filter['timeseries-tas-annual-mean'].values \
                                                      - df_filter_1960['timeseries-tas-annual-mean'].values

        # Max temp
        maxi = np.round(df_filter['timeseries-tas-annual-mean'].max(), 2)

        # Min temp
        mini = np.round(df_filter['timeseries-tas-annual-mean'].min(), 2)

        # Average temp
        average_temp = np.round(df_filter['timeseries-tas-annual-mean'].mean(), 2)

        return f'{maxi}°C', f'{mini}°C', f'{average_temp}°C'

    # ------------------------------------------------------------------------------------------------------------------
    # Callback for updating the time series of the geo map.
    @app.callback(
        Output('Time_plot_climate', 'figure'),
        Input('radio_items_time_climat', 'value'),
        Input('radio_items_format_climat', 'value'),
        Input('radio_items_measure_climat', 'value'),
        Input('year_selection_climat', 'value'))
    def update_time_climate_year(tipo, format, opcion, years):
        # By Year
        if format == 'Year':
            # X label
            x_label = 'Years'

            if tipo == 'World':
                # Grouping by year
                temp_by_year = df_climate_country.groupby(['year'])['mean_temp'].mean().to_frame().reset_index()
                # Range
                y_range = [18.8, 20.5]

                # Plotting year
                fig = px.line(temp_by_year, x="year", y="mean_temp", title='Temperature by Year (1960-2020)')

            elif tipo == 'Continents':
                # Grouping by year and continents
                temp_by_year_cont = df_climate_country.groupby(['year', 'Continent'])[
                    'mean_temp'].mean().to_frame().reset_index()
                # Range
                y_range = [7, 25.5]

                # Ploting
                fig = px.line(temp_by_year_cont, x="year", y="mean_temp", color='Continent',
                              title='Temperature by Continent (1960-2020)')
        # By month
        elif format == 'Month':
            # X label
            x_label = 'Months'

            if tipo == 'World' and opcion == 'Animation':
                # Grouping by year, month
                temp_subgroup = (df_climate_country.groupby(by=["year", "month"]).agg(
                    {'mean_temp': 'mean'}).reset_index())
                # Range
                y_range = [14, 24]

                # Ploting
                fig = px.line(temp_subgroup, x="month", y="mean_temp", animation_frame="year",
                              title="Average Temperature each Month of Every Year")

            elif tipo == 'World' and opcion == 'Static':
                # Grouping by year, month
                temp_subgroup = (
                    df_climate_country.groupby(by=["year", "month"]).agg({'mean_temp': 'mean'}).reset_index()
                        .rename(columns={'mean_Temp': 'Average of temperature'})
                )

                # Filtering by selection
                temp_subgroup = temp_subgroup[temp_subgroup['year'].isin(years)]

                fig = px.line(temp_subgroup, x="month", y="mean_temp", color="year",
                              title="Average temperature by month, Continent and year"
                              )
                # Range
                y_range = [14, 24]

                # Ploting
                fig = px.line(temp_subgroup, x="month", y="mean_temp", color="year",
                              title=f"Average Temperature each Month of {years}")

            elif tipo == 'Continents' and opcion == 'Animation':
                # Grouping by year, month, continents
                temp_subgroup = (df_climate_country.groupby(by=["year", "month", 'Continent']).agg(
                    {'mean_temp': 'mean'}).reset_index())
                # Range
                y_range = [-2, 28]

                # Ploting
                fig = px.line(temp_subgroup, x="month", y="mean_temp", color="Continent", animation_frame="year",
                              title="Average Temperature each Month of Every Year by Continent ")

        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"], template='seaborn',
                          xaxis_title=x_label,
                          yaxis_title='Mean Temperature °C',
                          yaxis_range=y_range)

        return fig

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------
    # Callback for updating the time series of the geo map.
    @app.callback(
        [Output('Correlation_plot', 'figure'),
         Output('adf_test_disaster', 'children'),
         Output('stationary_disaster', 'children'),
         Output('adf_test_climate', 'children'),
         Output('stationary_climate', 'children'),
         Output('correlation_message', 'children')],
        Input('differencing', 'value'),
        Input('disaster_type_correlation', 'value'))
    def correlation_plot(differencing, disaster_type, ):
        # Dataframes
        # Climate change
        temp_by_year = df_climate_country.groupby(['year'])['mean_temp'].mean().to_frame().reset_index()

        # Disaster
        # filtering by type of disasters
        if disaster_type == 'All':
            df_filter = df[df['Year'] <= 2020]
        else:
            df_filter1 = df[df['Year'] <= 2020]
            df_filter = df_filter1[df_filter1["Disaster Subgroup"] == disaster_type]

        # Frequency disaster
        disasters_by_year_aux = df_filter["Year"].value_counts().to_frame().reset_index()
        disasters_by_year_aux.columns = ["Year", "Count"]
        disasters_by_year_aux = disasters_by_year_aux.sort_values(by="Year", ascending=True)

        # filling the empty years
        empty_df = pd.DataFrame(data=range(1960, 2021), columns=['Year'])
        disasters_by_year = pd.merge(left=disasters_by_year_aux, right=empty_df, on='Year', how='right')
        disasters_by_year.fillna(0.001, inplace=True)

        if differencing == 'Zero':
            title = f'{disaster_type} Disaster and World Temperature'
        elif differencing == 'One diff + log(disaster)':
            # Climate
            temp_by_year['mean_temp'] = temp_by_year['mean_temp'].diff()
            # Disaster
            disasters_by_year['Count'] = np.log(disasters_by_year['Count']) \
                                         - np.log(disasters_by_year['Count']).shift(1)

            title = f'1 Diff on log Number {disaster_type} Disaster and ' \
                    f'1 Diff World Temperature'

        # Plot
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        # Disaster
        fig.add_trace(go.Scatter(x=disasters_by_year['Year'], y=disasters_by_year['Count'],
                                 mode='lines',
                                 name=f'{disaster_type} Disaster'),
                      secondary_y=False)

        # Climate change
        fig.add_trace(go.Scatter(x=temp_by_year['year'], y=temp_by_year['mean_temp'],
                                 mode='lines',
                                 name='Avg Temperature'),
                      secondary_y=True)

        # Set y-axes titles
        fig.update_yaxes(title_text="Disaster Frequency", secondary_y=False)
        fig.update_yaxes(title_text="Average Temperature °C", secondary_y=True)

        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"], template='seaborn',
                          xaxis_title='Year',
                          title=title)

        # Horizontal legend
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

        # --------------------------------------------------------------------------------------------------------------
        # ADF-test disaster
        result = stattools.adfuller(disasters_by_year['Count'].dropna(), autolag='AIC')
        adf_message = f'p-value: {result[1]:9.2f} '

        # Checking hypothesis
        if result[1] < 0.05:
            stationary_mess = "Reject Ho - Time Series is Stationary"
        else:
            stationary_mess = "Failed to Reject Ho - Time Series is Non-Stationary"

        # ADF-test climat
        result_climat = stattools.adfuller(temp_by_year['mean_temp'].dropna(), autolag='AIC')
        adf_message_climat = f'p-value: {result_climat[1]:9.2f} '

        # Checking hypothesis
        if result_climat[1] < 0.05:
            stationary_mess_climat = "Reject Ho - Time Series is Stationary"
        else:
            stationary_mess_climat = "Failed to Reject Ho - Time Series is Non-Stationary"

        # --------------------------------------------------------------------------------------------------------------
        # Correlation
        series_disaster = disasters_by_year['Count'].dropna().reset_index()['Count']
        # correlation = series_disaster.corr(temp_by_year['mean_temp'].dropna())

        # Cross-Correlation
        correlation = stattools.ccf(temp_by_year['mean_temp'].dropna().values, series_disaster.values)
        correlation_mess = f'The correlation is {correlation[0]:9.3f}'

        return fig, adf_message, stationary_mess, adf_message_climat, stationary_mess_climat, correlation_mess

    # Callback for updating the time series of the geo map.
    @app.callback(
        Output('Arima_plot', 'figure'),
        Input('Arima_select', 'value'))
    def arima_plot(dataset,):

        # Disasters
        if dataset == 'Disasters':
            title = 'Disaster Forecast using ARIMA'
            ylabel = "Disaster Frequency"

            # Frequency disaster
            df_filter = df[df['Year'] <= 2020]
            disasters_by_year = df_filter["Year"].value_counts().to_frame().reset_index()
            disasters_by_year.columns = ["Year", "Count"]
            disasters_by_year = disasters_by_year.sort_values(by="Year", ascending=True)

            # Setting index
            disasters_by_year["date"] = pd.to_datetime(disasters_by_year["Year"], format="%Y")
            disasters_by_year.set_index("date", inplace=True)

            # ----------------------------------------------------------------------------------------------------------
            # Create Training and Test
            serie_a_predecir = disasters_by_year['Count']
            serie_a_predecir.index.freq = 'AS'
            y_index = serie_a_predecir.index

        elif dataset == 'World Temperature':
            title = 'Average World Temperature Forecast using ARIMA'
            ylabel = "Temperature °C"

            # Climate change
            temp_by_year = df_climate_country.groupby(['year'])['mean_temp'].mean().to_frame().reset_index()

            # Setting index
            temp_by_year["date"] = pd.to_datetime(temp_by_year["year"], format="%Y")
            temp_by_year.set_index("date", inplace=True)

            # ----------------------------------------------------------------------------------------------------------
            # Create Training and Test
            serie_a_predecir = temp_by_year['mean_temp']
            serie_a_predecir.index.freq = 'AS'
            y_index = serie_a_predecir.index

        # --------------------------------------------------------------------------------------------------------------
        # 90% split
        size_train = int(len(y_index) * 0.9)

        train = serie_a_predecir[y_index[:size_train]]
        test = serie_a_predecir[y_index[size_train:len(y_index)]]

        # Arima Model
        if dataset == 'Disasters':
            model = ARIMA(train, order=(1, 2, 2))
            lower = "lower Count"
            upper = "upper Count"
        elif dataset == 'World Temperature':
            model = ARIMA(train, order=(2, 1, 2))
            lower = "lower mean_temp"
            upper = "upper mean_temp"

        # Fit model
        model_fit = model.fit()

        # Forecast
        forecast = model_fit.get_forecast(len(y_index) - size_train + 5)  # 95% conf
        forecast_series = forecast.predicted_mean
        forecast_conf_int = forecast.conf_int(alpha=0.05)

        # ----------------------------------------------------------------------------------------------------------
        # Plot
        fig = go.Figure()
        # Disaster
        fig.add_trace(go.Scatter(x=train.index, y=train,
                                 mode='lines',
                                 name='Training')
                      )
        fig.add_trace(go.Scatter(x=test.index, y=test,
                                 mode='lines',
                                 name='Actual')
                      )
        # Prediction
        fig.add_trace(go.Scatter(x=forecast_series.index, y=forecast_series,
                                 mode='lines',
                                 name='Prediction')
                      )

        # noinspection PyTypeChecker
        fig.add_trace(go.Scatter(x=forecast_conf_int.index, y=forecast_conf_int[lower],
                                 mode="lines",
                                 showlegend=False,
                                 line_color='rgba(255,127,0,0.0)',
                                 name='Lower_level'))

        # noinspection PyTypeChecker
        fig.add_trace(go.Scatter(x=forecast_conf_int.index, y=forecast_conf_int[upper],
                                 fill='tonexty', mode="lines",
                                 fillcolor='rgba(255,127,0, 0.2)',
                                 line_color='rgba(255,127,0,0)',
                                 showlegend=False,
                                 name='Upper_Level'))

        # Set y-axes titles
        fig.update_yaxes(title_text=ylabel)

        # Title and configuration
        fig.update_layout(modebar_add=["v1hovermode", "toggleSpikeLines"], template='seaborn',
                          xaxis_title='Year',
                          title=title)

        return fig
