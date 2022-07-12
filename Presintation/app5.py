from flask import Flask
app = Flask(__name__)

# Create an instance of Flask
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd


# Route to the basic info
@app.route('/sunburst')
def sunburst():
    # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/...')
    df=pd.read_csv("OKcupid_cleaned_up.csv")

    starbucks_dist = df.groupby(by=["location", "job", "offspring",]).count()[["income"]].rename(columns={"income":"Count"})
    starbucks_dist["okcupid"] = "okcupid"
    starbucks_dist = starbucks_dist.reset_index()

    fig = px.sunburst(starbucks_dist, path=["okcupid", "location", "job", "offspring", ], values='Count',
                  title="Sunburst OkCupid", width=1000, height=800)
    fig.show()(df, x='Date', y='AAPL.High')
    return  html.Div([dcc.Graph(figure=fig)])


@app.route('/chart')
def chart():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/...')
    fig = px.line(df, x='Date', y='AAPL.High')
    return  html.Div([dcc.Graph(figure=fig)])
    
if __name__ == "__main__":
    app.run()
