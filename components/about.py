# Project DS4A - Team 40
# Udjat webApp - tabs components dash
# June 05 2022

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc
# ----------------------------------------------------------------------------------------------------------------------
udjat = '''
We are team 40, the creator of **Udjat**, a diverse and empowered team with great ideas.  Climate change is a reality.
 It affects us all and it will be more impactful in the coming years. One of the factors that will increase is natural
  disasters related to climate change. These disasters generate high human and economic costs which can be mitigated 
  with proper preparation. Understanding the effect of external factors such as climate change on natural disasters is 
  vital to generating strategies to diminish such costs.

Visualizing the frequency and location of natural disasters and their possible correlation with climate change will 
allow the world to prepare for future events and create awareness that this is a real issue and we all have a part 
in avoiding further disasters and their impact.  This is the reason for the existence of **Udjat**. 

* **Udjat** - the Eye of Horus - is a protective symbol against danger.
* **Udjat** represents an all-seeing, protective eye looking out for natural disasters. 
'''


jm = '''
**[Juan Felipe Monsalvo](https://www.linkedin.com/in/jmonsalvo/)** is a Mechanical Engineer who graduated from 
EAFIT University - Colombia and the ENIT – France.
 He characterize himself as a curious person who is always learning something new, from artificial intelligence to 
 blockchain and guitar solos. He is currently working as a "Data Scientist" at Organización Corona, where He has 
 led and participated in the creation and deployment of different projects. Ranging from artificial vision models 
 for customer services and quality inspection, to forecast models and predictive maintenance and quality models for 
 the company.
'''

malcolm = '''
**[Malcolm Giraldo](https://www.linkedin.com/in/malcolm-giraldo-serna-a33a3325/)** is a Cloud Engineer with experience
 working with AWS, Linux Operative Systems, Application Servers and
 CICD tools. He has worked with several technology companies on many different roles from Support Engineer to
  Team Leader. He enjoys video games, playing his guitars and reading fantasy books. 
'''

sandra = '''
**[Sandra Barreto](https://www.linkedin.com/in/sandra-barreto-1b9646235/)** is a statistician with teaching 
experience, using virtual teaching tools and R software. She has the 
ability to guide students in projects where statistics is a way to achieve the proposed objectives. She likes to learn 
and share what She has learned, now She is learning about data science to update the methodologies She use.
'''
# ----------------------------------------------------------------------------------------------------------------------
# Dash content
# ----------------------------------------------------------------------------------------------------------------------
def about_gui():
    return html.Div([
        # Title
        html.H2('About Us', style={"margin-left": "5px", 'margin-bottom': '20px'}),

        # Udjat
        dcc.Markdown(children=udjat),

        html.Br(),

        # Members
        dbc.Row(
            [  # Picture
                dbc.Col(html.H1([html.Img(src='./assets/Malcolm.png',
                                          id='profile0',
                                          style={'height': '70%', 'width': '60%'},
                                          ),
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Description
                dbc.Col(dcc.Markdown(children=malcolm), width=10
                        ),
            ],
            id='member0', align="center",
        ),
        dbc.Row(
            [  # Picture
                dbc.Col(html.H1([html.Img(src='./assets/Sandra.png',
                                          id='profile1',
                                          style={'height': '60%', 'width': '60%'},
                                          ),
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Description
                dbc.Col(dcc.Markdown(children=sandra), width=10
                        ),
            ],
            id='member1', align="center",
        ),
        dbc.Row(
            [  # Picture
                dbc.Col(html.H1([html.Img(src='./assets/JuanMonsalvo.png',
                                          id='profile2',
                                          style={'height': '60%', 'width': '60%'},
                                          ),
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Description
                dbc.Col(dcc.Markdown(children=jm), width=10
                        ),
            ],
            id='member2', align="center",
        ),
        # dbc.Row(
        #     [  # Picture
        #         dbc.Col(html.H1([html.Img(src='./assets/JuanMonsalvo.png',
        #                                   id='profile3',
        #                                   style={'height': '60%', 'width': '60%'},
        #                                   ),
        #                          ], style={'textAlign': 'center'}
        #                         ), width=2
        #                 ),
        #         # Description
        #         dbc.Col(dcc.Markdown(children=jm), width=10
        #                 ),
        #     ],
        #     id='member3', align="center",
        # ),
        # dbc.Row(
        #     [  # Picture
        #         dbc.Col(html.H1([html.Img(src='./assets/JuanMonsalvo.png',
        #                                   id='profile4',
        #                                   style={'height': '60%', 'width': '60%'},
        #                                   ),
        #                          ], style={'textAlign': 'center'}
        #                         ), width=2
        #                 ),
        #         # Description
        #         dbc.Col(dcc.Markdown(children=jm), width=10
        #                 ),
        #     ],
        #     id='member4', align="center",
        # ),
        # dbc.Row(
        #     [  # Picture
        #         dbc.Col(html.H1([html.Img(src='./assets/JuanMonsalvo.png',
        #                                   id='profile5',
        #                                   style={'height': '60%', 'width': '60%'},
        #                                   ),
        #                          ], style={'textAlign': 'center'}
        #                         ), width=2
        #                 ),
        #         # Description
        #         dbc.Col(dcc.Markdown(children=jm), width=10
        #                 ),
        #     ],
        #     id='member5', align="center",
        #),
    ])

# ----------------------------------------------------------------------------------------------------------------------
