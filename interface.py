import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from visualization_functions import *
import pandas as pd
import plotly.graph_objs as go

items = pd.read_csv("Data/items.csv")
reviews = pd.read_csv("Data/reviews.csv")
review_item = reviews.join(items.set_index('asin'), on='asin', how='inner', lsuffix='_review', rsuffix='_item')
helpful_vote = review_item.sort_values('helpfulVotes', ascending=False).drop_duplicates(['asin'])
brands = sorted(list(set(review_item["brand"])))
len_brand = len(brands)

def create_df(helpful_vote):
    list = {}
    for i in brands:
        list[i] = helpful_vote[helpful_vote['brand'] == i]
    return list
df = create_df(helpful_vote)

fnameDict = {
    'ASUS': df["ASUS"]["asin"],
    'Apple': df["Apple"]["asin"],
    'Google': df["Google"]["asin"],
    'HUAWEI': df["HUAWEI"]["asin"],
    'Motorola': df['Motorola']["asin"],
    'Nokia': df['Nokia']["asin"],
    'OnePlus': df['OnePlus']["asin"],
    'Samsung': df['Samsung']["asin"],
    'Sony': df['Sony']["asin"],
    'Xiaomi': df['Xiaomi']["asin"]
}

names = list(fnameDict.keys())

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        [
            html.H1(id="project_title", style={"textAlign": "center"},
                    children="Visualization of cell phone reviews data"),
            html.Br(),
            dcc.Graph(id="sales_volume", figure=brand_counts(review_item)),
            html.Br(),
            dcc.Graph(id="overall_rating", figure=plot_stacked_rating_hist_allbrands(review_item)),
            html.Br(),
            html.Div([
                dcc.Dropdown(
                    id='brand_dropdown',
                    options=[{'label': name, 'value': name} for name in brands],
                    style={'height': '30px', 'width': '100px'},
                    value='ASUS',
                    clearable=False,
            ),
            ],style={'width': '20%', 'display': 'inline-block'}),

            dcc.Graph(id="brand_rating")
        ]
    ),
    html.H2(id="Vote_title",
            children="Highest vote reviews  selecting cell phone",
            style={"textAlign": "center"}),
    html.Div(
    [
        html.Div([
        dcc.Dropdown(
            id='name-dropdown',
            options=[{'label':name, 'value':name} for name in names],
            placeholder="Select a brand",
            value = list(fnameDict.keys())[0]
            ),
            ],style={'width': '20%', 'display': 'inline-block'}),

        html.Div([
        dcc.Dropdown(
            id='item-dropdown',
            placeholder="Select a type",
            ),
            ],style={'width': '20%', 'display': 'inline-block'}
        ),
        html.Hr(),
        html.Div(id='display-selected-values')
    ]
    ),
])

@app.callback(
    Output('brand_rating', 'figure'),
    [Input('brand_dropdown', 'value')])
def update_brand_rating(brand_name):
    filtered_df = review_item[review_item.brand == brand_name]
    print(filtered_df.head())
    ratings = filtered_df.groupby('rating_review').size().reset_index(name='counts')
    ratings['counts'] = ratings['counts']

    data = go.Data([go.Pie(labels=list(ratings['rating_review']), values=list(ratings['counts']))])
    layout = go.Layout(title={"text":"Pie chart of "+brand_name+"'s ratings",
                              'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
                       font={"size":16})
    figure = go.Figure(data=data, layout=layout)

    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'lightblue']
    figure.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=16,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    return figure

@app.callback(
    dash.dependencies.Output('item-dropdown', 'options'),
    [dash.dependencies.Input('name-dropdown', 'value')]
)
def update_date_dropdown(name):
    return [{'label': i, 'value': i} for i in fnameDict[name]]

@app.callback(
    dash.dependencies.Output('display-selected-values', 'children'),
    [dash.dependencies.Input('item-dropdown', 'value')])
def set_display_children(selected_value):
    res = ""
    res += helpful_vote.loc[helpful_vote['asin'] == selected_value]['body']
    return res


if __name__ == '__main__':
    app.run_server(debug=True)
