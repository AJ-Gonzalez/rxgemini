"""Test Module for fetcher"""

import os
import unittest
import pathlib

from rxgemini.storage import (
    get_relative_path,
    timestamp, path_handler, store_instance, LoggedInstance)


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

    def test_path_handler(self):
        """
        Tests path handler function
        """
        test_var = path_handler("main.py")
        self.assertIsInstance(test_var, pathlib.Path)

    def test_store_instance(self):
        """
        Tests instance storage
        """
        test_str = """
        Sample muiltiline
        string
        """
        ts_var = timestamp()
        inst_var = LoggedInstance("sample_name",
                                  ts_var[1], ts_var[0],
                                  "sample_caller", "main.py", [
                                  ],
                                  test_str, {}, {}, [], True)
        test_var = store_instance(inst_var)
        self.assertIsInstance(test_var, str)
        os.remove(test_var)


if __name__ == "__main__":
    unittest.main()
