"""Data fetcher module for rxgemini"""

import functools
import inspect
import pathlib
import sys

import typer

from rxgemini.configurator import config_checker
from rxgemini.errors import ScopeGetterException

CONFIG = config_checker(internal=True)


MARKER_KW = CONFIG["MARKER_KW"]
TAGS = CONFIG["TAGS"]


def timestamp():
    pass


def path_handler_for_tests(cwd: str):
    # make this windows and unix compatible
    pass


def cache_writer(path_str, obj_name, input_label, input_tuple):
    # (args, kwargs)
    pass

    # pickle binaries
    # metadata to json


def data_fetcher(func: callable) -> callable:
    @functools.wraps
    def wrapper_fetcher(*args, **kwargs):
        obj_name = func.__name__
        src_file = inspect.getfile(func)
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
