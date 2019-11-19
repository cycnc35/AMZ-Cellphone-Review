import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

# print(df.head())
items = pd.read_csv("Data/items.csv")
brands = sorted(list(set(items["brand"])))


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(id="project_title", style={"textAlign": "center"},
            children="Cell phone reviews"),

    dcc.Graph(id="brand_rating"),
    dcc.Slider(
        id="brand_slider",
        min=0,
        max=len(brands)+1,
        step=None,
        marks=dict([(i+1,name) for i, name in enumerate(brands)]),
        value=1
    ),
    html.Br(),
    dcc.Graph(id='graph-with-slider'),

    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])

@app.callback(
    Output('brand_rating', 'figure'),
    [Input('brand_slider', 'value')])
def update_brand_rating(brand_idx):
    filtered_df = items[items.brand == brands[brand_idx-1]]
    print(filtered_df.head())
    ratings = filtered_df.groupby('rating').size().reset_index(name='counts')
    print(type(ratings))
    print(ratings)

    return {
        'data': [
            go.Bar(x=list(ratings['rating']), y=list(ratings['counts']))
        ],
        'layout': {}
    }




@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log', 'title': 'GDP Per Capita',
                   'range':[2.3, 4.8]},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition = {'duration': 500},
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)