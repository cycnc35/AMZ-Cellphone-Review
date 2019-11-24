"""
This module mainly use "dash" package to provide user with a friendly interface for
visualization of cell phone reviews.
"""

import pandas as pd
import plotly.graph_objs as go
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from visualization_functions import brand_counts, plot_stacked_rating_hist_allbrands, create_df


def data_preprocessing(items, reviews):
    """
    Do data pre-processing, merge to data into one named "review_item"
    Extract the highest vote for review and create another table named "helpful_vote"

    :param items: dataframe, csv file
    :param reviews: dataframe, csv file

    :return review_item: dataframe, merge two data source
            helpful_vote: dataframe, with highest helpful vote
            brands: list, brand name of each cell phone
            helpful_vote_df: dataframe, each type of cellphone with highest vote
    """

    review_item = reviews.join(items.set_index('asin'), on='asin', how='inner', lsuffix='_review'
                               , rsuffix='_item')
    helpful_vote = review_item.sort_values('helpfulVotes', ascending=False).\
        drop_duplicates(['asin'])
    brands = sorted(list(set(review_item["brand"])))

    helpful_vote_dict = create_df(helpful_vote, brands)
    return review_item, helpful_vote, brands, helpful_vote_dict

def main():
    """
    This function run the dash package. Create a html component. The structure of the
    DOM object is a big div includes two children div. One for the chart part the other for
    searching reviews.
    """
    items = pd.read_csv("Data/items.csv")
    reviews = pd.read_csv("Data/reviews.csv")
    review_item, helpful_vote, brands, helpful_vote_dict = data_preprocessing(items, reviews)

    helpful_vote_dict = {
        'ASUS': helpful_vote_dict["ASUS"]["asin"],
        'Apple': helpful_vote_dict["Apple"]["asin"],
        'Google': helpful_vote_dict["Google"]["asin"],
        'HUAWEI': helpful_vote_dict["HUAWEI"]["asin"],
        'Motorola': helpful_vote_dict['Motorola']["asin"],
        'Nokia': helpful_vote_dict['Nokia']["asin"],
        'OnePlus': helpful_vote_dict['OnePlus']["asin"],
        'Samsung': helpful_vote_dict['Samsung']["asin"],
        'Sony': helpful_vote_dict['Sony']["asin"],
        'Xiaomi': helpful_vote_dict['Xiaomi']["asin"]
    }

    names = list(helpful_vote_dict.keys())

    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.Div(
            [
                html.H1(id="project_title", style={"textAlign": "center"},
                        children="Visualization of cell phone reviews data"),
                html.Div([
                    html.P('This website provides user with a detail reviews from Amazon. Included '
                           '"Sales percentage" from Amazon website, satisfaction histogram in '
                           'different brands.'),
                    html.P('User can select a certain brand to see the total satisfaction. Also, '
                           'selecting a certain type of cell phone, the website will provides the '
                           'highest vote review from Amazon.')
                ], style={'width': '60%', 'margin': "auto", 'text-align': 'center'}),
                html.Br(),
                dcc.Graph(id="sales_volume", figure=brand_counts(review_item)),
                html.Br(),
                dcc.Graph(id="overall_rating",
                          figure=plot_stacked_rating_hist_allbrands(review_item)),
                html.Br(),
                html.Div(
                    [
                        dcc.Dropdown(
                            id='brand_dropdown',
                            options=[{'label': name, 'value': name} for name in brands],
                            style={'height': '30px', 'width': '100px'},
                            value='ASUS',
                            clearable=False,
                        ),
                    ], style={'width': '20%', 'display': 'inline-block'}),
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
                        options=[{'label': name, 'value': name} for name in names],
                        placeholder="Select a brand",
                        value=list(helpful_vote_dict.keys())[0],
                        clearable=False
                    ), ], style={'width': '20%', 'display': 'inline-block'}),
                html.Div([
                    dcc.Dropdown(
                        id='item-dropdown',
                        placeholder="Select a type",
                        clearable=False
                    ), ], style={'width': '20%', 'display': 'inline-block'}),
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
        ratings = filtered_df.groupby('rating_review').size().reset_index(name='counts')
        ratings['counts'] = ratings['counts']

        data = go.Data([go.Pie(labels=list(ratings['rating_review']),
                               values=list(ratings['counts']))])
        layout = go.Layout(title={"text": "Pie chart of " + brand_name + "'s ratings",
                                  'x': 0.5, 'y': 0.9, 'xanchor': 'center', 'yanchor': 'top'},
                           font={"size": 16})
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
        return [{'label': i, 'value': i} for i in helpful_vote_dict[name]]

    @app.callback(
        dash.dependencies.Output('display-selected-values', 'children'),
        [dash.dependencies.Input('item-dropdown', 'value')])
    def set_display_children(selected_value):
        res = ""
        res += helpful_vote.loc[helpful_vote['asin'] == selected_value]['body']

        return res

    app.run_server(debug=True)


if __name__ == '__main__':
    main()
