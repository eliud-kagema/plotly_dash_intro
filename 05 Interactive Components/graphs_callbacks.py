import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as objs
import pandas as pd


df = pd.read_csv('../data/gapminderDataFiveYear.csv')
print(df.head())