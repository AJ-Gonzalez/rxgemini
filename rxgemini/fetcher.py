"""Data fetcher module for rxgemini"""

import functools
import inspect

import typer

MARKER_KW = "placeholder for config"
TAGS = {"FETCHER": ["fetcher", "on", "off"]}


def path_handler_for_tests(cwd: str):
    pass


def data_fetcher(func):
    @functools.wraps
    def wrapper_fetcher(*args, **kwargs):
        obj_name = func.__name__
        src_file = inspect.getfile(func)
        # refactor this as its own parser engine
        with open(src_file) as runfile:
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
        
