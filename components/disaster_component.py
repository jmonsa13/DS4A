# Project DS4A - Team 40
# Udjat webApp - Disaster_component

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc

from components.data_component import *


# ----------------------------------------------------------------------------------------------------------------------
# Function
# ----------------------------------------------------------------------------------------------------------------------
# Function to redirect the type of container to use
def disaster_analisis(analisis_type):
    if analisis_type == 'Geo-Type':
        return geo_plot_layout()
    elif analisis_type == 'Time-Series':
        return time_series_plot_layout()
    elif analisis_type == 'Animation-Plot':
        return animation_disas_plot_layout()


# Function to change the filter
def disaster_analisis_selector(analisis_type):
    if analisis_type == 'Geo-Type':
        return geo_plot_layout_selector()
    elif analisis_type == 'Time-Series':
        return timeseries_layout_selector()


# ----------------------------------------------------------------------------------------------------------------------
# Geo_plot
# ----------------------------------------------------------------------------------------------------------------------
# Geoplot layout selector
def geo_plot_layout_selector():
    layout = [
        dbc.Col(
            [
                html.P("Select an option:", style={'font-weight': 'bold'}),
                dcc.RadioItems(id='radio_items', options=['Continents', 'Countries'],
                               value='Continents',
                               inline=True,
                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                           'margin-left': '20px'})
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
        dbc.Col(
            [
                html.P("Select a type of disaster:", style={'font-weight': 'bold'}),
                dcc.Dropdown(id='disaster_type_dropdown', options=disaster_subgroup_list,
                             value=disaster_subgroup_list[-1])
            ], width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)',
                               "margin-left": "5px"}, id='second_selector'
        ),
        dbc.Col(
            [
                html.P("Select a format:", style={'font-weight': 'bold'}),
                dcc.Dropdown(id='geo_items_format', options=['Frequency', 'Economical Impact'],
                             value='Frequency')
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
    ]

    return layout


# Geoplot layout
def geo_plot_layout():
    # Main plot
    layout = [dbc.Col(dcc.Graph(id='Geo_map', hoverData={'points': [{'location': 'North America'}]}), width=6),
              # Second plot
              dbc.Col(dcc.Graph(id='Time_series'), width=6)
              ]
    return layout


# ----------------------------------------------------------------------------------------------------------------------
# Time Series_plot
# ----------------------------------------------------------------------------------------------------------------------
# Geoplot layout selector
def timeseries_layout_selector():
    layout = [
        dbc.Col(
            [
                html.P("Select a visualization:", style={'font-weight': 'bold'}),
                dcc.RadioItems(id='radio_items_time', options=['All disasters', 'By type'],
                               value='All disasters',
                               inline=True,
                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                           'margin-left': '20px'})
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
        dbc.Col(
            [
                html.P("Select a format:", style={'font-weight': 'bold'}),
                dcc.RadioItems(id='radio_items_format', options=['Frequency', 'Economical Impact'],
                               value='Frequency',
                               inline=True,
                               labelStyle={'display': 'block', 'cursor': 'pointer',
                                           'margin-left': '20px'})
            ],
            width=3, style={'backgroundColor': 'rgba(211, 211, 211, 0.4)', "margin-left": "10px"},
        ),
        dbc.Col(children=[
            html.Br(),
            dcc.RadioItems(id='radio_items_measure', options=['Sum', 'Mean'],
                           value='Sum',
                           inline=True,
                           labelStyle={'display': 'block', 'cursor': 'pointer',
                                       'margin-left': '20px'})
        ],
            width='auto', style={"margin-left": "10px"},
            id='agg_function_selector'
        )

    ]

    return layout


# Time_series layout
def time_series_plot_layout():
    # Main plot
    layout = dbc.Col(dcc.Graph(id='Total_disaster'), width=12)

    return layout

# Animation_disaster_plot_layout
def animation_disas_plot_layout():
    # Filtering
    disaster_subgroup_df = (df_disaster.groupby(by=["Year", "Disaster Subgroup", "Disaster Type"]).agg(
        {'ISO': 'count', 'Total Deaths': 'sum'}).reset_index()
                            .rename(columns={'ISO': 'Number of Disasters'})
                            )
    disaster_subgroup_df["Total Deaths"] = np.log(disaster_subgroup_df["Total Deaths"] + 1)

    # Adding a minimum value to make visibly the legen
    disaster_subgroup_df.at[0, 'Total Deaths'] = 0.001

    fig = px.scatter(disaster_subgroup_df, x="Number of Disasters", y="Total Deaths", animation_frame="Year",
                     animation_group="Disaster Type",
                     color="Disaster Subgroup", size="Total Deaths", size_max=30, range_y=[0, 20], range_x=[0, 250],
                     hover_name="Disaster Type",
                     title="Log(Total Deaths) vs Number of Disaster by Year,type and Subtype of Disaster",
                     )
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    fig.layout.update(showlegend=True)

    # Main plot
    layout = dbc.Col(dcc.Graph(id='Animation_disaster', figure=fig), width=12)

    return layout
