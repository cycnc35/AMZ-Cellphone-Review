"""
Test module for functions in visualization_functions.py
"""
import unittest
import pandas as pd
import os
from ..visualization_functions import data_preprocessing, comp_stacked_rating_hist_allbrands,\
     create_helpful_vote_dict


item_path = "./AMZ_Cellphone_Review/data/items.csv"
review_path = "./AMZ_Cellphone_Review/data/reviews.csv"


class UnitTests(unittest.TestCase):
    """
    This class contains test functions to test whether visualization_functions.py
    works correctly, including preprocessing, computing statistics, operating data frames.
    """
    def test_data_preprocessing(self):
        """
        Test for prep_data to check whether the merged data frame
        is of correct dimensions
        """
        print(os.getcwd())
        items = pd.read_csv(item_path)
        reviews = pd.read_csv(review_path)
        review_item, _, _, _ = data_preprocessing(items, reviews)
        self.assertEqual(review_item.shape[1], items.shape[1]+reviews.shape[1]-1)
        self.assertEqual(review_item.shape[0], reviews.shape[0])

    def test_create_helpful_vote_dict(self):
        """
        Test for create_helpful_vote_dict to check whether columns in helpful_vote_dict
        are the same as those of helpful_vote, also check whether total length of
        helpful_vote_dict equals to length of helpful_vote.
        """
        items = pd.read_csv(item_path)
        reviews = pd.read_csv(review_path)
        review_item = reviews.join(items.set_index('asin'), on='asin', how='inner',
                                   lsuffix='_review', rsuffix='_item')
        helpful_vote = review_item.sort_values('helpfulVotes', ascending=False). \
            drop_duplicates(['asin'])
        brands = sorted(list(set(review_item["brand"])))
        helpful_vote_dict = create_helpful_vote_dict(helpful_vote, brands)
        total_len = 0  # accumulate length of each element in helpful_vote_dict
        same_columns = True
        for key in helpful_vote_dict:
            total_len += helpful_vote_dict[key].shape[0]
            if list(helpful_vote_dict[key].columns) != list(helpful_vote.columns):
                same_columns = False

        self.assertEqual(helpful_vote.shape[0], total_len)
        self.assertTrue(same_columns)

    def test_comp_stacked_rating_hist_allbrands(self):
        """
        Tests for comp_stacked_rating_hist_allbrands to check whether
        each list in freq_dict sums to one.
        """
        items = pd.read_csv(item_path)
        reviews = pd.read_csv(review_path)
        review_item, _, _, _ = data_preprocessing(items, reviews)
        _, _, freq_dict = comp_stacked_rating_hist_allbrands(review_item)
        sums_to_one = True
        for key in freq_dict:
            if sum(freq_dict[key]) != 1.0:
                sums_to_one = False
                break
        self.assertTrue(sums_to_one)


if __name__ == '__main__':
    unittest.main()
