import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['This is the Outer Most Div',
                            html.Div(['This is an inner Div'], 
                            style={'color':'red'})],    
                        style={'color':'green', 'border': '2px green solid'}


)

if __name__ == '__main__':
    app.run_server()