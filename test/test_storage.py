"""Test Module for fetcher"""

import unittest
import pathlib

from rxgemini.storage import get_relative_path, timestamp


class TestStorage(unittest.TestCase):
    """
    Tests methods/functions from rxgemini/storage.py

    Args:
        unittest (class): Inherits from TestCase
    """

    def test_get_relative_path(self):
        """
        Tests relative path getter
        """
        path_var = pathlib.Path().cwd()
        self.assertIsInstance(get_relative_path(
            path_var), pathlib.Path)

    def test_timestamp(self):
        """
        Tests timestamp function
        """
        ts_var = timestamp()
        self.assertIsInstance(ts_var, tuple)
        self.assertEqual(len(ts_var), 2)
        self.assertIsInstance(ts_var[0], str)
        self.assertIsInstance(ts_var[1], float)


if __name__ == "__main__":
    unittest.main()
