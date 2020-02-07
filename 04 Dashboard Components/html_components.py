import dash
import dash_html_components as html

app = dash.Dash()

app.Layout = html.Div([
    'This is the Outer Most Div'
])

if __name__ == '__main__':
    app.run_server()