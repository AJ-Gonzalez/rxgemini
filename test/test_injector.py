"""Test Module for injector"""

import unittest

from rxgemini.injector import (
    path_handler_for_tests
)


class TestInjector(unittest.TestCase):
    """
    Tests methods/functions from rxgemini/injector.py

    Args:
        unittest (class): Inherits from TestCase
    """

    def test_path_handler_for_tests(self):
        """
        Tests Path handler function
        """
        self.assertIsInstance(path_handler_for_tests(), int)


if __name__ == "__main__":
    unittest.main()
