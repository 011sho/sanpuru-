import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('assets/data.csv')

dates = []
for _date in df['date']:
    date = datetime.datetime.strptime(_date, '%Y/%m/%d').date()
    dates.append(date)

n_subscribers = df['subscribers'].values
n_reviews = df['reviews'].values

diff_subscribers = df['subscribers'].diff().values
diff_reviews = df['reviews'].diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H2(children='PythonによるWebスクレイピング～Webアプリケーション編～'),
    html.Div(children=[
        dcc.Graph(
            id='subscriber_graph',
            figure={
               'data':[
                   go.Scatter(
                       x=dates,
                       y=n_subscribers,
                       mode='lines+markers',
                       name='受講生総数',
                       opacity=0.7,
                       yaxis='y1'    
                   )
               ]
            }
        )
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
