import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from flask import Flask, render_template_string
from dash import Dash, dcc, html, Input, Output
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load data
csv_path = Path("2022-2023.csv")
crashes_df = pd.read_csv(csv_path, low_memory=False)

# Flask app
server = Flask(__name__)

# Dash app
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Define layout of Dash app
app.layout = html.Div([
    html.H1("Crash Analysis Dashboard"),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='correlation-heatmap'),
    dcc.Graph(id='average-injuries-bar'),
])

# Callback for updating bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    Input('bar-chart', 'id')
)
def update_bar_chart():
    crash_type_counts = crashes_df["FIRST_CRASH_TYPE"].value_counts()
    fig = px.bar(x=crash_type_counts.index, y=crash_type_counts.values, labels={'x': 'Crash Type', 'y': 'Count'},
                 title='Crash Type Counts')
    return fig

# Callback for updating correlation heatmap
@app.callback(
    Output('correlation-heatmap', 'figure'),
    Input('correlation-heatmap', 'id')
)
def update_correlation_heatmap():
    selected_columns = ['FIRST_CRASH_TYPE', 'INJURIES_TOTAL']
    correlation_data = crashes_df[selected_columns]
    correlation_data = pd.get_dummies(correlation_data, columns=['FIRST_CRASH_TYPE'], drop_first=True)
    correlation_matrix = correlation_data.corr()
    fig = px.imshow(correlation_matrix, title='Correlation Matrix')
    return fig

# Callback for updating average injuries bar chart
@app.callback(
    Output('average-injuries-bar', 'figure'),
    Input('average-injuries-bar', 'id')
)
def update_average_injuries_bar():
    mean_injuries_per_type = crashes_df.groupby('FIRST_CRASH_TYPE')['INJURIES_TOTAL'].mean().sort_values().reset_index()
    fig = px.bar(mean_injuries_per_type, x='INJURIES_TOTAL', y='FIRST_CRASH_TYPE', orientation='h',
                 title='Average Injuries Total by First Crash Type',
                 labels={'INJURIES_TOTAL': 'Average Injuries Total', 'FIRST_CRASH_TYPE': 'First Crash Type'})
    return fig

# Flask route for serving dashboard
@server.route('/')
def serve_dashboard():
    return app.index()

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8050, debug=True)
