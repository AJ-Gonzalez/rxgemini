"""Test Module for fetcher"""

import unittest
import pathlib
from typing import Any

from rxgemini.fetcher import (
    path_handler_for_tests,
    data_fetcher,
    call_data_handler)

# Testbench functions


def no_args():
    """
    Test function with no args, kwargs, or anything.

    Returns:
        None: Literally none
    """
    return None


def one_arg(sample_arg: Any) -> Any:
    """

    Test function with one sample positional argument

    Args:
        sample_arg (Any): Sample positional arg

    Returns:
        Any : same value
    """
    return sample_arg


def multi_arg(sample_arg: str, sample_other_arg: int) -> tuple:
    """

    Test function with multiple positional arguments

    Args:
        sample_arg (str): Sample Arg
        sample_other_arg (int): sample arg

    Returns:
        _type_: _description_
    """
    return (sample_arg, sample_other_arg)


def multi_kwarg(
        sample_arg: str = "sample", sample_other_arg: int = 155) -> tuple:
    """
    Test function with multiple kewyword arguments

    Args:
        sample_arg (str, optional): Sample arg. Defaults to "sample".
        sample_other_arg (int, optional): Sample arg. Defaults to 155.

    Returns:
        tuple : sample
    """
    return (sample_arg, sample_other_arg)


def mix_arg_kwarg(
        sample_arg: str = "sample", sample_other_arg: int = 155) -> tuple:
    """
    Test function with mix positional and keyword arguments

    Args:
        sample_arg (str, optional): Sample arg. Defaults to "sample".
        sample_other_arg (int, optional): Sample arg. Defaults to 155.

    Returns:
        tuple: sample
    """
    return (sample_arg, sample_other_arg)


# Testbench class with above functions as methods:

class SampleMethodsClass:
    """
    A class of sample methods to simulate method calls in testing
    for RX Gemini.
    """

    def __init__(self):
        self.sample_const: int = 777

    @data_fetcher
    def no_args(self):
        """
        Test function with no args, kwargs, or anything.

        Returns:
            None: Literally none
        """
        return None

    def one_arg(self, sample_arg: Any) -> Any:
        """

        Test function with one sample positional argument

        Args:
            sample_arg (Any): Sample positional arg

        Returns:
            Any : same value
        """
        return sample_arg

    def multi_arg(self, sample_arg: str, sample_other_arg: int) -> tuple:
        """

        Test function with multiple positional arguments

        Args:
            sample_arg (str): Sample Arg
            sample_other_arg (int): sample arg

        Returns:
            _type_: _description_
        """
        return (sample_arg, sample_other_arg)

    def multi_kwarg(self,
                    sample_arg: str = "sample",
                    sample_other_arg: int = 155) -> tuple:
        """
        Test function with multiple kewyword arguments

        Args:
            sample_arg (str, optional): Sample arg. Defaults to "sample".
            sample_other_arg (int, optional): Sample arg. Defaults to 155.

        Returns:
            tuple : sample
        """
        return (sample_arg, sample_other_arg)

    def mix_arg_kwarg(self,
                      sample_arg: str = "sample",
                      sample_other_arg: int = 155) -> tuple:
        """
        Test function with mix positional and keyword arguments

        Args:
            sample_arg (str, optional): Sample arg. Defaults to "sample".
            sample_other_arg (int, optional): Sample arg. Defaults to 155.

        Returns:
            tuple: sample
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
        obj = SampleMethodsClass()
        value = obj.no_args()
        # Confirms decorator does not alter functionality
        self.assertEqual(value, None)

    def test_call_data_handler_regarding_noarg_functions(self):
        """
        Tests call values organizer on fucntion calls
        """
        # check against None
        self.assertIsNot(call_data_handler(no_args, [], {}), None)
        self.assertIsInstance(call_data_handler(no_args, [], {}), dict)
        result = call_data_handler(no_args, [], {})
        # Confirm 3 items in dict
        self.assertEqual(len(result), 3)

    def test_call_data_handler_regarding_one_arg_functions(self):
        """
        Tests call values organizer on fucntion calls
        """
        # check against None
        result = call_data_handler(one_arg, [22], {})
        # Confirm 3 items in dict
        self.assertEqual(len(result), 3)
        result = call_data_handler(one_arg, [], {"one_arg": 22})
        # Confirm 3 items in dict
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()
