"""
Test module for functions in preprocess.py
"""
import unittest
import os
import pandas as pd
from ..preprocessing import data_preprocessing


item_path = "./amz_cellphone_review/data/items.csv"
review_path = "./amz_cellphone_review/data/reviews.csv"


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

        self.assertEqual(review_item.shape[1], items.shape[1] + reviews.shape[1] - 1)

    def test_data_preprocessing_2(self):
        """
        Test for prep_data to check whether the merged data frame
        is of correct dimensions
        """
        print(os.getcwd())
        items = pd.read_csv(item_path)
        reviews = pd.read_csv(review_path)
        review_item, _, _, _ = data_preprocessing(items, reviews)

        self.assertEqual(review_item.shape[0], reviews.shape[0])

    def test_data_preprocessing_3(self):
        """
        Test for prep_data to check whether the 'brands' has the same length
        """
        print(os.getcwd())
        items = pd.read_csv(item_path)
        reviews = pd.read_csv(review_path)
        review_item, _, brands, _ = data_preprocessing(items, reviews)
        nums_brands = len(sorted(list(set(review_item["brand"]))))

        self.assertEqual(nums_brands, len(brands))


if __name__ == '__main__':
    unittest.main()
