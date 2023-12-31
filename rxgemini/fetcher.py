"""Data fetcher module for rxgemini"""

import functools
import inspect
import pathlib
import sys

from datetime import datetime
from typing import Any


from rxgemini.configurator import config_checker
from rxgemini.errors import ScopeGetterException
from rxgemini.log_handler import log_warning, log_info, pretty_print
from rxgemini.storage import LoggedInstance, store_instance
from rxgemini.constants import LOGGING_OPTS

CONFIG = config_checker(internal=True)


MARKER_KW = CONFIG["MARKER_KW"]
TAGS = CONFIG["TAGS"]
SAVE_DIR = CONFIG["SAVE_DIRECTORY"]
LOG_MODE = CONFIG["LOG_MODE"]


def get_args_dict(
        fn: callable,
        args: list, kwargs: dict, is_method: bool = False) -> dict:
    """
    Fetches data values from function

    Args:
        fn (callable): _description_
        args (list): _description_
        kwargs (dict): _description_
        is_method (bool, optional): _description_. Defaults to False.

    Returns:
        dict: _description_
    """   
    if is_method:
        args_names = fn.__code__.co_varnames[1: fn.__code__.co_argcount]
    else:
        args_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    return {**dict(zip(args_names, args), **kwargs)}


def call_data_handler(
        func: callable,
        args: list,
        kwargs: dict) -> dict:
    """
    Handler for func/method call data,
    Takes in the func, args, and kwargs
    Extracts expected types, recieved types,
    and recieved values.

    Args:
        func (callable): func/method
        args (list): positional args from func/method
        kwargs (dict): keyword args from func/method

    Returns:
        dict: function input values by argument, function actual types
              function expected types
    """
    signature = inspect.signature(func)
    if "self" in str(signature):
        log_info("Working with method")
    log_info(f"Recieved signature: {signature} from {func.__name__}")
    log_info(f"Call with args: {args}  and kwargs: {kwargs}")
    try:
        expected_types: dict = inspect.get_annotations(func)
    except AttributeError as ex_msg:
        log_warning(f"Running on python version <3.10 since: {ex_msg}")
        log_warning("Using legacy method")
        # Annotations are the fist member of the function object members
        # It is a tuple in which the first member is just "__annotations__"
        members = inspect.getmembers(func)
        expected_types: dict = members[0][1]

    values = {}
    for idx, key in enumerate(expected_types):
        if key != "return":
            log_info(f"Checking for parameter: {key}")
            try:
                param: Any = kwargs[key]
                log_info(f"Keyword arg value found: {param}")
                values[key] = param
            except KeyError as ex_msg:
                log_info(f"{ex_msg} is is a positional arg.")
                try:
                    values[key] = args[idx]
                except IndexError as ex_message:
                    log_info(
                        f"No positional args or all were scanned {ex_message}")

    res_dict: dict = {}
    res_dict["expected_types"] = expected_types
    res_dict["in_vals"] = values
    res_dict["call_types"] = {key: type(value)
                              for key, value in expected_types.items()}
    return res_dict


def get_arg_vars(func: callable) -> dict:
    """

    Gets argument variable names

    Args:
        func (callable): Function or method object

    Returns:
        dict: dictionary of args
    """
    print(inspect.signature(func))
    arg_dict = {}
    return arg_dict


def timestamp() -> tuple:
    """
    Provides formatted timestamps for metadata.

    Returns:
        tuple: Human readable, unix format
    """
    t_stamp = datetime.now()
    human_readable: str = str(t_stamp).split(".", maxsplit=1)[0]
    unix_readable: float = t_stamp.timestamp()
    return (human_readable, unix_readable)


def check_if_enabled(src_file: str) -> bool:
    """

    Checks if the fetcher is enabled in python module

    With syntax: # MARKER_KW fetcher on/off

    Args:
        src_file (str): Absolute path to source file

    Returns:
        bool: Fetcher enabled or disabled.
    """
    with open(src_file, "r", encoding="utf-8") as runfile:
        for line in runfile:
            # Allow flags at any indent level
            line = line.lstrip()
            if line.startswith("#") and MARKER_KW in line:
                line = line.replace(MARKER_KW, "")
                line = line.replace("#", "")
                line = line.strip()
                if line.split(" ")[0] == TAGS["FETCHER"][0]:
                    fetcher_setting = line.split(" ")[1]
                    if fetcher_setting == TAGS["FETCHER"][1]:
                        log_info("Starting data fetch")
                        return True
                    if fetcher_setting == TAGS["FETCHER"][2]:
                        log_info("Skipping data fetch")
                        return False
    log_warning("No explicit keyword found, skipping fetch by default")
    return False


def path_handler_for_tests(src_name: str) -> str:
    """
    Path handler function

    Args:
        src_name (str): source file

    Returns:
        str: save path
    """
    file_name = str(pathlib.Path(src_name).name).replace(".py", "")
    cwd = pathlib.Path().cwd()
    test_save_path = pathlib.Path(cwd, "test", SAVE_DIR, file_name)
    log_info(f"Save path for data: {test_save_path}")
    pathlib.Path(test_save_path).mkdir(parents=True, exist_ok=True)
    return test_save_path


def get_relative_path(absolute_path: str) -> pathlib.Path:
    """
    Gets path relative to CWD

    Args:
        absolute_path (str): abodulte path

    Returns:
        pathlib.Path: relative path
    """
    cwd = pathlib.Path().cwd()
    return pathlib.Path(absolute_path).relative_to(cwd)


def data_fetcher(func: callable) -> callable:
    """

    Data fetcher decorator to gather test data

    Args:
        func (callable): Function or method

    Raises:
        ScopeGetterException: A special error to graba stack trace

    Returns:
        callable: Called function/method
    """
    @functools.wraps(func)
    def wrapper_fetcher(*args, **kwargs):
        src_file = inspect.getfile(func)
        if check_if_enabled(src_file):
            obj_name = func.__name__
            src_code = inspect.getsource(func)
            if LOG_MODE == LOGGING_OPTS[1]:
                log_info("Analyzing source code from: \n")
                pretty_print(src_code)
            caller_name = ""
            try:
                raise ScopeGetterException
            except ScopeGetterException as expected:
                frame = sys.exc_info()[2].tb_frame.f_back
                caller_name = frame.f_code.co_name
                log_info(f"Obtained stack trace: {expected}")
                fn_data: dict = call_data_handler(func, args, kwargs)
            if "test_" in caller_name:
                ret_val = func(*args, **kwargs)
                log_info("Skipping since this is a test method")
                return ret_val

            fn_data: dict = call_data_handler(func, args, kwargs)
            ts_tup = timestamp()
            ret_val = func(*args, **kwargs)
            call_obj = LoggedInstance(
                obj_name, ts_tup[1], ts_tup[0],
                caller_name, get_relative_path(src_file),
                get_relative_path(
                    src_file).parts,
                inspect.getdoc(func),
                fn_data["expected_types"],
                fn_data["call_types"],
                fn_data["in_vals"], ret_val)
            print(call_obj)
            call_path = store_instance(call_obj)
            log_info(f"Fetched call, storing in: {call_path}")
            return ret_val

        ret_val = func(*args, **kwargs)
        return ret_val

    return wrapper_fetcher
