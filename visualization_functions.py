"""
This module provides helper function for interface.py.
"brand_counts" and "plot_stacked_rating_hist_allbrands" use "ployly" package to draw chart.
"create_helpful_vote_dict" create a dataframe with each highest vote for certain types
of cell phone
"""
import plotly.graph_objs as go


def brand_counts(review_item):
    """
    Plot a pie chart describing sales amount of all cellphone brands.

    :param review_item: a merged data frame of reviews and items
    :return: a pie chart describing sales amount of all cellphone brands
    """
    count = review_item.groupby("brand").size()
    labels = count.index
    values = count.values
    data = go.Data([go.Pie(labels=labels, values=values)])
    layout = go.Layout(title={"text": "Sales Volume", 'x': 0.5, 'y': 0.9, 'xanchor': 'center',
                              'yanchor': 'top'}, font={"size": 20})
    figure = go.Figure(data=data, layout=layout)

    return figure


def plot_stacked_rating_hist_allbrands(review_item):
    """
    Plot a stacked histogram of ratings for all brands.

    :param review_item: a merged data frame of reviews and items
    :return: a stacked histogram of ratings for all brands
    """
    brands = sorted(list(set(review_item["brand"])))
    scores = sorted(list(set(review_item["rating_review"])))

    freq_dict = dict()
    for brand_name in brands:
        filtered_df = review_item[review_item.brand == brand_name]
        ratings = filtered_df.groupby('rating_review').size().reset_index(name='counts')
        ratings['counts'] = ratings['counts'] / len(filtered_df)
        freq_dict[brand_name] = list(ratings['counts'])

    traces = []
    for i, score in enumerate(scores):
        trace = go.Bar(x=brands, y=[freq_dict[brand][i] for brand in brands], name=str(score))
        traces.append(trace)

    layout = go.Layout(title={'text': "Frequency histogram of all brands' ratings ",
                              'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'},
                       font={"size": 16}, barmode="stack")
    figure = go.Figure(data=traces, layout=layout)

    return figure


def create_helpful_vote_dict(helpful_vote, brands):
    """
    Create a list of dataframe

    :param helpful_vote: dataframe, Highest vote review for cell phone
    :param brands: list, brand name of cell phone
    :return: list of dataframe for highest vote review
    """
    vote_dict = {}
    for i in brands:
        vote_dict[i] = helpful_vote[helpful_vote['brand'] == i]
    return vote_dict
