"""Test Module for fetcher"""

import unittest

from rxgemini.fetcher import path_handler_for_tests


class TestFetcher(unittest.TestCase):
    """
    Tests methods/functions from rxgemini/fetcher.py

    Args:
        unittest (class): Inherits from TestCase
    """

    def test_path_handler_for_tests(self):
        """
        Tests path handling function
        """
        self.assertIsInstance(path_handler_for_tests("main.py"), str)


if __name__ == "__main__":
    unittest.main()
