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
def register_callbacks(app, df):
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
