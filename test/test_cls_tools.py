"""Test Module for fetcher"""

import unittest

from rich import print as pprint
from rxgemini.cls_tools import index_finder, instance_ranking


class TestClsTools(unittest.TestCase):
    """
    Tests methods/functions from rxgemini/cls_tools.py

    Args:
        unittest (class): Inherits from TestCase
    """

    def test_index_finder(self):
        """
        Tests complexity index finder
        """
        sample_dict = {
            "arg0": 123,
            "arg1": "hello there",
            "arg2": [
                1, 2, 3, 5, 6, 3, 5, 6, 7, 78, 789, 000],
            "arg3": IOError}
        self.assertIsInstance(index_finder(sample_dict), int)

    def test_instance_ranking(self):
        """
        Tests instance complexity ranker
        """
        test_data = ["23_hello", "11_world", "5_hello", "1_world",
                     "28_hello", "66_world", "133_hello", "50_world",
                     "30_hello", "60_world", "90_hello", "68_world",
                     "2_hello", "1_world", "10_hello", "20_world"]
        test_run = instance_ranking(test_data)
        pprint(test_run)
        self.assertIsInstance(test_run, dict)
        expected = {
            '50th': 30,
            'high': 133,
            'low': 1,
            '90th': 133,
            '10th': 5,
            '70th': 66,
            '30th': 20,
            'whole': [
                1, 2, 5, 10, 11, 20, 23, 28, 30, 50, 60, 66, 68, 90, 133],
            'raw': {
                1: '1_world',
                2: '2_hello',
                5: '5_hello',
                10: '10_hello',
                11: '11_world',
                20: '20_world',
                23: '23_hello',
                28: '28_hello',
                30: '30_hello',
                50: '50_world',
                60: '60_world',
                66: '66_world',
                68: '68_world',
                90: '90_hello',
                133: '133_hello'
            }
        }
        self.assertEqual(test_run, expected)


if __name__ == "__main__":
    unittest.main()
