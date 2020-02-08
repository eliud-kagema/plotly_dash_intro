import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my_id', value='Initial text', type='text'),
    html.Div(id='my-div')
])


if __name__ == '__main__':
    app.run_server()