import pandas as pd
import plotly.express as px
from flask import Flask, Response
from dash import Dash, html, dcc, callback, Output, Input



df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

server = Flask(__name__)
app = Dash(__name__, server=server)

@server.route('/health', methods=['GET'])
def ping():
    """
    Determine if the container is healthy.
    """
    return Response(response='{"status": "healthy"}', status=200, mimetype='application/json')

app.layout = html.Div([
    html.H1(children='Sample Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)
