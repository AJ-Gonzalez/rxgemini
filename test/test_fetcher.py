"""Test Module for fetcher"""

import unittest
import pathlib
import inspect
from typing import Any

from rxgemini.fetcher import (
    path_handler_for_tests,
    data_fetcher,
    in_types_handler,
    call_organizer)

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

    def test_call_organizer_regarding_functions(self):
        """
        Tests call values organizer on fucntion calls
        """
        # check against None
        sig = inspect.signature(no_args)
        print(sig)
        self.assertIsNot(call_organizer(sig, [], {}), None)
        self.assertIsInstance(call_organizer(sig, [], {}), dict)
        result = call_organizer(sig, [], {})
        # Confirm 3 items in dict
        self.assertEqual(len(result), 3)

    def test_call_organizer_regarding_methods(self):
        """
        Tests call values organizer on method calls
        """
        # check against None
        obj = SampleMethodsClass()
        sig = inspect.signature(obj.no_args)
        print(sig, obj)
        self.assertIsNot(call_organizer(sig, [], {}), None)
        self.assertIsInstance(call_organizer(sig, [], {}), dict)
        result = call_organizer(sig, [], {})
        # Confirm 3 items in dict
        self.assertEqual(len(result), 3)


if __name__ == "__main__":
    unittest.main()
