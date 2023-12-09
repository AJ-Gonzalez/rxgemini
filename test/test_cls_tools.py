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
        test_data = ["23+hello", "11+world", "5+hello", "1+world",
                     "28+hello", "66+world", "133+hello", "50+world",
                     "30+hello", "60+world", "90+hello", "68+world",
                     "2+hello", "1+world", "10+hello", "20+world"]
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
                1,
                2,
                5, 10, 11, 20, 23, 28, 30, 50, 60, 66, 68, 90, 133],
            'raw': {
                1: '1+world',
                2: '2+hello',
                5: '5+hello',
                10: '10+hello',
                11: '11+world',
                20: '20+world',
                23: '23+hello',
                28: '28+hello',
                30: '30+hello',
                50: '50+world',
                60: '60+world',
                66: '66+world',
                68: '68+world',
                90: '90+hello',
                133: '133+hello'
            }
        }
        self.assertEqual(test_run, expected)


if __name__ == "__main__":
    unittest.main()
