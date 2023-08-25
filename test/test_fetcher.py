"""Test Module for fetcher"""

import unittest
import pathlib
import inspect
from typing import Any

from rxgemini.fetcher import (
    path_handler_for_tests,
    data_fetcher,
    in_types_handler)

# Testbench functions


def no_args():
    """
    Test function with no args, kwargs, or anything.

    Returns:
        None: Literally none
    """
    return None


def one_arg(sample_arg: Any):
    """

    Test function with one sample positional argument

    Args:
        sample_arg (Any): Sample positional arg

    Returns:
        Any : same value
    """
    return sample_arg


def multi_arg(sample_arg: str, sample_other_arg: int):
    """

    Test function with one sample positional argument

    Args:
        sample_arg (Any): Sample positional arg

    Returns:
        Any : same value
    """
    return (sample_arg, sample_other_arg)


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
        self.assertIsInstance(path_handler_for_tests("main.py"), pathlib.Path)

    def test_fetcher_function(self):
        """
        Tests data fetcher function

        """
        # RXGEMINI fetcher on
        @data_fetcher
        def sample_func(param0: str, param1: int) -> bool:
            if param0 == "a" and param1 != 0:
                return True
            return False

        value = sample_func("a", 1)
        # Confirms decorator does not alter functionality
        self.assertEqual(value, True)

    def test_in_types_handler(self):
        """
        Tests handler for input types
        """
        def sample_func(param0: str, param1: int) -> bool:
            if param0 == "a" and param1 != 0:
                return True
            return False
        args = ["a", 1]
        in_types = [type(arg) for arg in args]
        handler = in_types_handler(inspect.signature(sample_func), in_types)
        print(handler)

    def test_call_organizer_regarding_fucntions(self):
        """
        Tests call values organizer
        """
        pass


if __name__ == "__main__":
    unittest.main()
