import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../data/mpg.csv')

app = dash.Dash()


features = df.columns
# ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight','acceleration', 'model_year', 'origin', 'name']
     

app.layout = html.Div([
            # First drop down
            html.Div([
                dcc.Dropdown(id='xaxis',
                    options=[{'label': i, 'value': i} for i in features],
                    value='displacement'
                )
            ], style={'width':'48%', 'display': 'inline-block'}),


            # Second drop down
           html.Div([
                dcc.Dropdown(id='yaxis',
                    options=[{'label': i, 'value': i} for i in features],
                    value='mpg'
                )
            ], style={'width':'48%', 'display': 'inline-block'}),




            dcc.Graph(id='feature-graphic')

], style={'padding': 10})