"""Test Module for fetcher"""

import unittest

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
        self.assertEqual(instance_ranking(test_data), None)


if __name__ == "__main__":
    unittest.main()
