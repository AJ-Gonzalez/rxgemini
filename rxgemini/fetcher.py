"""Data fetcher module for rxgemini"""

import functools
import inspect
import pathlib
import sys
import json
import pickle
from datetime import datetime
from typing import Union, Optional

import typer
from rich import print as pprint

from rxgemini.configurator import config_checker
from rxgemini.errors import ScopeGetterException

CONFIG = config_checker(internal=True)


MARKER_KW = CONFIG["MARKER_KW"]
TAGS = CONFIG["TAGS"]
SAVE_DIR = CONFIG["SAVE_DIRECTORY"]


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
            if line.startswith("#") and MARKER_KW in line:
                line = line.replace(MARKER_KW, "")
                line = line.replace("#", "")
                line = line.strip()
                if line.split(" ")[0] == TAGS["FETCHER"][0]:
                    fetcher_setting = line.split(" ")[1]
                    if fetcher_setting == TAGS["FETCHER"][1]:
                        typer.echo("starting fetch")
                        return True
                    elif fetcher_setting == TAGS["FETCHER"][2]:
                        typer.echo("skipping fetch")
                        return False
    typer.echo("No keyword found, skipping fetch by default")
    return False


def path_handler_for_tests():
    # make this windows and unix compatible
    pass


def cache_writer(
    f_path: str,
    obj_name: str,
    role_label: str,
    cache_data: Union[str, tuple],
    meta_mode: Optional[bool] = False,
):
    # (args, kwargs)
    if meta_mode:
        # need to figure out how to do everything path related with pathlib
        f_name = "dummy"
        with open(f_name, "w", encoding="utf-8") as cache:
            json.dump(cache_data, cache, indent=4)
        return f_name
    else:
        f_name = "dummy"
        with open(f_name, "wb") as cache:
            pickle.dump(cache_data, cache)
        return f_name

    # needs refactoring and retooling to accept data

    # pickle binaries
    # metadata to json


def data_fetcher(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper_fetcher(*args, **kwargs):
        src_file = inspect.getfile(func)
        if check_if_enabled(src_file):
            obj_name = func.__name__
            src_code = inspect.getsource(func)
            pprint(src_code)
            pprint(src_file, obj_name)
            ret_value = func(*args, **kwargs)
            return ret_value
        else:
            ret_value = func(*args, **kwargs)
            return ret_value

        # refactor this as its own parser engine
        with open(src_file, "r", encoding="utf-8") as runfile:
            for line in runfile:
                if line.startswith("#") and MARKER_KW in line:
                    line = line.replace(MARKER_KW, "")
                    line = line.replace("#", "")
                    line = line.strip()
                    if line.split(" ")[0] == TAGS["FETCHER"][0]:
                        fetcher_setting = line.split(" ")[1]
                        if fetcher_setting == TAGS["FETCHER"][1]:
                            typer.echo("starting fetch")
                        elif fetcher_setting == TAGS["FETCHER"][2]:
                            typer.echo("skipping fetch")
                            ret_value = func(*args, **kwargs)
                            return ret_value
        cwd = str(pathlib.Path.cwd())
        # this will need a reforctor to work on windows
        path_str = path_handler_for_tests(cwd)
        caller_name = ""
        try:
            raise ScopeGetterException
        except ScopeGetterException as expected:
            frame = sys.exc_info()[2].tb_frame.f_back
            caller_name = frame.f_code.co_name
            typer.echo(expected)

        if "test_" in caller_name:
            ret_value = func(*args, **kwargs)
            typer.echo("Skipping")
        else:
            input_fname = cache_writer()
            # redo cache writer to fit new smart approach
            ret_value = func(*args, **kwargs)
            output_fname = cache_writer(path_str, obj_name, label_var, return_val)
            ts_tup = timestamp()
            meta_fname = cache_writer(meta_mode=True)
        return ret_value

    return wrapper_fetcher
