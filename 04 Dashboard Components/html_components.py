import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['This is the Outer Most Div'],
                        style={'color':'green', 'border': '2px green solid'}


)

if __name__ == '__main__':
    app.run_server()