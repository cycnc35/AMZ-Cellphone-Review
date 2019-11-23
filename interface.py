import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go


items = pd.read_csv("Data/items.csv")
reviews = pd.read_csv("Data/reviews.csv")
review_item = reviews.join(items.set_index('asin'), on='asin', how='inner', lsuffix='_review', rsuffix='_item')

print(review_item.columns)
brands = sorted(list(set(review_item["brand"])))
len_brand = len(brands)

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(id="project_title", style={"textAlign": "center"},
            children="Visualization of cell phone reviews data"),
    html.Br(),
    dcc.Dropdown(
        id='brand_dropdown',
        options=[{'label': name, 'value': name} for name in brands],
        value='ASUS'
    ),
    dcc.Graph(id="brand_rating")
    # dcc.Slider(
    #     id="brand_slider",
    #     min=0,
    #     max=len_brand+1,
    #     step=None,
    #     marks=dict([(i+1,name) for i, name in enumerate(brands)]),
    #     value=1
    # )

])

@app.callback(
    Output('brand_rating', 'figure'),
    [Input('brand_dropdown', 'value')])
def update_brand_rating(brand_name):
    filtered_df = review_item[review_item.brand == brand_name]
    print(filtered_df.head())
    # print(filtered_df.head())
    ratings = filtered_df.groupby('rating_review').size().reset_index(name='counts')
    ratings['counts'] = ratings['counts'] / len(filtered_df)
    print(ratings)
    data = go.Data([go.Bar(x=list(ratings['rating_review']), y=list(ratings['counts']))])
    layout = go.Layout(title={"text":"ratings distribution of " + brand_name, "xanchor": "left"}, font={"size":20})
    figure = go.Figure(data=data, layout=layout)

    return figure





if __name__ == '__main__':
    app.run_server(debug=True)
