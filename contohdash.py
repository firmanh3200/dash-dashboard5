# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:54:01 2019

@author: Nitin
"""

# Import Necessary Libraries related to HTML tags and various core components like slider, checboxes, dropdowns etc.
import time
import dash
from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash_bootstrap_templates import load_figure_template, ThemeChangerAIO, template_from_url
import plotly.express as px
import pandas as pd

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

#Code to start an application
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Templets
templates = [ "bootstrap", "cerulean", "cosmo", "cyborg", "darkly", 
             "flatly", "journal", "litera", "lumen", "lux", "materia", 
             "minty", "morph", "pulse", "quartz", "sandstone", "simplex", 
             "sketchy", "slate", "solar", "spacelab", "superhero", "united", 
             "vapor", "yeti", "zephyr" ]

templates_dark = ['bootstrap_dark', 'cerulean_dark', 'cosmo_dark', 
                  'cyborg_dark', 'darkly_dark', 'flatly_dark', 'journal_dark', 
                  'litera_dark', 'lumen_dark', 'lux_dark', 'materia_dark', 
                  'minty_dark', 'morph_dark', 'pulse_dark', 'quartz_dark', 
                  'sandstone_dark', 'simplex_dark', 'sketchy_dark', 
                  'slate_dark', 'solar_dark', 'spacelab_dark', 
                  'superhero_dark', 'united_dark', 'vapor_dark', 
                  'yeti_dark', 'zephyr_dark']

#HTML layout and Graph components are defined in this section
df = pd.DataFrame(
    {
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
    }
)
header = html.H4(
    "Indikator Pembangunan Jawa Barat", 
    className="bg-primary text-white p-4 mb-2 text-center"
)
footer = html.Footer(
    "Copyright 2024 @ BPS Provinsi Jawa Barat", 
    className="bg-primary text-white p-4 mb-2 text-center"
)

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary"),
        dbc.Button("Secondary", color="secondary"),
        dbc.Button("Success", color="success"),
        dbc.Button("Warning", color="warning"),
        dbc.Button("Danger", color="danger"),
        dbc.Button("Info", color="info"),
        dbc.Button("Light", color="light"),
        dbc.Button("Dark", color="dark"),
        dbc.Button("Link", color="link"),
    ],
    className="m-4",
)
graph1 = html.Div(dcc.Graph(id="graph1"), className="m-4")
graph2 = html.Div(dcc.Graph(id="graph2"), className="m-4")

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(ThemeChangerAIO(aio_id="theme", 
                                        radio_props={"value":dbc.themes.FLATLY}), width=2,),
                dbc.Col(buttons),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.Col(graph1,width="100%", id="kotak1"),
                ), width={'size':5},
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.Col(graph2,width="100%", id="kotak2"),
                ), width={'size':5},
                ),
                
            ]
        ),
        footer,
    ],
    className="m-4 dbc",
    fluid=True,
)

@app.callback(
    Output("graph1", "figure"), Output("graph2", "figure"), 
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_graph_theme(theme):
    return px.bar(
        df, x="Fruit", y="Amount", color="City", barmode="group", template=template_from_url(theme)
    )

#Code to run the application
if __name__ == '__main__':
    app.run_server(debug = True)