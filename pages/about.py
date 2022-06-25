# Project DS4A - Team 40
# Udjat webApp - About us components dash

# ----------------------------------------------------------------------------------------------------------------------
# Library
# ----------------------------------------------------------------------------------------------------------------------
from dash import html, dcc
import dash_bootstrap_components as dbc

from dash_labs.plugins import register_page

# dash-labs plugin call, menu name and route
register_page(__name__, path='/us')
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

luis = '''
**[Luis Ruiz](https://www.linkedin.com/in/luis-humberto-ruiz-ponce-4b3008144/?locale=en_US)** is a tech savvy marketer 
with great passion for business. He holds an Economics degree and works on marketing 
analytics for Pinterest. Luis is on a continuous learning path and is convinced that Data Science is a great tool on his
 mission to spot market trends and support businesses growth. In his free time he enjoys activities such as boxing, 
 sharing quality time with family and friends, and traveling. 
'''

guillermo = '''
**Guillermo Giraldo** is a Environmental Engineer with a Management Specialization with long experience on sanitary 
services. He is a focused worker who likes to achieve his objectives in a clear way. He likes to learn and study, 
even if the contents of his studies don't relate to his career knowledge.
'''

christian = '''
**[Christian Fuertes](www.linkedin.com/in/christian-fuertes-4b10301b7)** is a Physiscs and Biology student in Los
 Andes University,
 with basic knowledge of Python, Java and C++, currently learning about data science, with the purpose of applying it 
 to his future professional career, as it supposes an incredibly useful and required tool nowadays, that expands one's 
 capabilities at the time of investigation in pure sciences, for example in astrophysical or microbiological
  research. He likes to play sports, listen to music, investigate about diverse topics, play the piano, and go 
  hiking or walk through natural landscapes.
'''
# ----------------------------------------------------------------------------------------------------------------------
# Layout
# ----------------------------------------------------------------------------------------------------------------------
# specific layout for this page
layout = dbc.Container(
    html.Div([
        # Title
        html.H2('About Us', style={"margin-left": "5px", 'margin-bottom': '20px'}),

        # Udjat
        dcc.Markdown(children=udjat),

        html.Br(),

        # Members 1
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

        # Members 2
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

        # Members 3
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

        # Members 4
        dbc.Row(
            [  # Picture
                dbc.Col(html.H1([html.Img(src='./assets/Luis.jpg',
                                          id='profile3',
                                          style={'height': '60%', 'width': '60%'},
                                          ),
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Description
                dbc.Col(dcc.Markdown(children=luis), width=10
                        ),
            ],
            id='member3', align="center",
        ),

        # Members 5
        dbc.Row(
            [  # Picture
                dbc.Col(html.H1([html.Img(src='./assets/Guillermo.jpg',
                                          id='profile4',
                                          style={'height': '60%', 'width': '60%'},
                                          ),
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Description
                dbc.Col(dcc.Markdown(children=guillermo), width=10
                        ),
            ],
            id='member4', align="center",
        ),

        # Members 6
        dbc.Row(
            [  # Picture
                dbc.Col(html.H1([html.Img(src='./assets/christian.jpg',
                                          id='profile5',
                                          style={'height': '60%', 'width': '60%'},
                                          ),
                                 ], style={'textAlign': 'center'}
                                ), width=2
                        ),
                # Description
                dbc.Col(dcc.Markdown(children=christian), width=10
                        ),
            ],
            id='member5', align="center",
        ),
    ])
)
# ----------------------------------------------------------------------------------------------------------------------
