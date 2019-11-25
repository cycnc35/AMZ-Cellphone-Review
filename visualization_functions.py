"""
This module provides helper function for interface.py.
"brand_counts" and "plot_stacked_rating_hist_allbrands" use "ployly" package to draw chart.
"create_helpful_vote_dict" create a dataframe with each highest vote for certain types
of cell phone
"""
import plotly.graph_objs as go


def data_preprocessing(items, reviews):
    """
    Do data pre-processing, merge to data into one named "review_item"
    Extract the highest vote for review and create another table named "helpful_vote"

    :param items: dataframe, csv file
    :param reviews: dataframe, csv file

    :return review_item: dataframe, merge two data source
            helpful_vote: dataframe, with highest helpful vote
            brands: list, brand name of each cell phone
            helpful_vote_df: dataframe, highest vote for each type of cellphone
    """
    review_item = reviews.join(items.set_index('asin'), on='asin', how='inner', lsuffix='_review',
                               rsuffix='_item')
    helpful_vote = review_item.sort_values('helpfulVotes', ascending=False).\
        drop_duplicates(['asin'])
    brands = sorted(list(set(review_item["brand"])))

    helpful_vote_dict = create_helpful_vote_dict(helpful_vote, brands)
    return review_item, helpful_vote, brands, helpful_vote_dict


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


def comp_stacked_rating_hist_allbrands(review_item):
    """
    Compute rating distributions for all brands
    :param review_item: a merged data frame containing item and review info
    :return: brands: an ascending list containing names of all brands
             scores: an ascending list containing all possible ratings
             freq_dict: key is brand, value is rating distribution for this brand
    """
    brands = sorted(list(set(review_item["brand"])))
    scores = sorted(list(set(review_item["rating_review"])))

    freq_dict = dict()
    for brand_name in brands:
        filtered_df = review_item[review_item.brand == brand_name]
        ratings = filtered_df.groupby('rating_review').size().reset_index(name='counts')
        ratings['counts'] = ratings['counts'] / len(filtered_df)
        freq_dict[brand_name] = list(ratings['counts'])

    return brands, scores, freq_dict


def plot_stacked_rating_hist_allbrands(review_item):
    """
    Plot a stacked histogram of ratings for all brands.
    :param review_item: a merged data frame of reviews and items
    :return: a stacked histogram of ratings for all brands
    """
    brands, scores, freq_dict = comp_stacked_rating_hist_allbrands(review_item)
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
    for name in brands:
        vote_dict[name] = helpful_vote[helpful_vote['brand'] == name]
    return vote_dict
