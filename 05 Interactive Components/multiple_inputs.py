import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('../data/mpg.csv')

print(df.tail())