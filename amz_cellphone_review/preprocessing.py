"""
This module provides function to process data files.
"create_helpful_vote_dict" create a data frame with highest vote for each type of cell phones
"data_preprocessing" merges items and reviews by product id
"""


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