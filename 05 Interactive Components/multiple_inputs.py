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
                [Input('xaxis', 'value'),
                Input('yaxis', 'value')
                ]
)
def update_graph(x_axis_name, y_axis_name):
    return {
            'data': [go.Scatter(
                                x=df[x_axis_name], 
                                y=df[y_axis_name], 
                                text=df['name']
                                mode='markers',
                                marker= {'size': 15})
                                ],

            'layout':go.Layout(title='MPG Dashboard'),
                                xaxis={'title':x_axis_name},
                                yaxis={'title':y_axis_name},
        }

if __name__ == '__main__':
    app.run_server()