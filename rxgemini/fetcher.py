"""Data fetcher module for rxgemini"""
# pylint: skip-file
# Skipping file because of pending refactor
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
INPUT_LBL = CONFIG["INPUT_SUFFIX"]
OUTPUT_LBL = CONFIG["OUTPUT_SUFFIX"]
META_LABEL = CONFIG["METADATA_SUFFIX"]


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
    test_save_path = pathlib.Path(cwd, "tests", SAVE_DIR, file_name)
    typer.echo(test_save_path)
    pathlib.Path(test_save_path).mkdir(parents=True, exist_ok=True)
    return test_save_path

    # make this windows and unix compatible


def write_cache(
    f_path: str,
    obj_name: str,
    role_label: str,
    cache_data: Union[str, tuple],
    t_stamp: str,
    meta: Optional[bool] = False,
):
    """
    Cahce writer, (will be replaced in upcoming refactor)

    Args:
        f_path (str): _description_
        obj_name (str): _description_
        role_label (str): _description_
        cache_data (Union[str, tuple]): _description_
        t_stamp (str): _description_
        meta (Optional[bool], optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    if meta:
        # need to figure out how to do everything path related with pathlib
        f_name = f"{t_stamp}{obj_name}{role_label}.json"
        save_path = pathlib.Path(f_path, f_name)
        if not pathlib.Path(save_path).exists():
            with open(save_path, "w", encoding="utf-8") as cache:
                json.dump(cache_data, cache, indent=4)
        return save_path
    else:
        f_name = f"{t_stamp}{obj_name}{role_label}.pickle"
        save_path = pathlib.Path(f_path, f_name)
        with open(save_path, "wb") as cache:
            pickle.dump(cache_data, cache)
        return save_path


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
            pprint(src_code)
            pprint(src_file, obj_name)
            f_path = path_handler_for_tests(src_file)
            caller_name = ""
            try:
                raise ScopeGetterException
            except ScopeGetterException as expected:
                frame = sys.exc_info()[2].tb_frame.f_back
                caller_name = frame.f_code.co_name
                typer.echo(expected)

            if "test_" in caller_name:
                ret_val = func(*args, **kwargs)
                typer.echo("Skipping")
            else:
                ts_tup = timestamp()
                params: tuple = (args, kwargs)
                input_fn = write_cache(
                    f_path, obj_name, INPUT_LBL, params, ts_tup[1])
                typer.echo(input_fn)
                ret_val = func(*args, **kwargs)
                output_fn = write_cache(
                    f_path, obj_name, OUTPUT_LBL, ret_val, ts_tup[1]
                )
                typer.echo(output_fn)
                in_types = [str(type(arg)) for arg in args]
                kwarg_types = [str(type(arg)) for arg in kwargs]
                print(in_types, kwarg_types)
                print(inspect.signature(func))
                metadata = {
                    "name": obj_name,
                    "timestamp_unix": ts_tup[1],
                    "timestamp_human": ts_tup[0],
                    "file": str(get_relative_path(src_file)),
                    "file_path_parts": get_relative_path(src_file).parts,
                    "docstring": inspect.getdoc(func),
                    "in_types": in_types,
                    "kwarg_types": kwarg_types,
                    "out_type": str(type(ret_val)),
                }

                meta_fname = write_cache(
                    f_path,
                    obj_name, META_LABEL, metadata, ts_tup[1], meta=True
                )
                typer.echo(meta_fname)
                return ret_val
        else:
            ret_val = func(*args, **kwargs)
            return ret_val

    return wrapper_fetcher
