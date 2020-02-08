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


@app.callback(Output('feature-graphic', 'figure'),
                [
                    Input('xaxis', 'value'),
                    Input('yaxis', 'value')
                ]
)

def update_graph(xaxis_name, yaxis_name):
    return {
        'data': [go.Scatter(
            x=df[xaxis_name],
            y=df[yaxis_name],
            text=df['name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={'title': xaxis_name.title()},
            yaxis={'title': yaxis_name.title()},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()