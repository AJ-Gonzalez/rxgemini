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
INPUT_LABEL = CONFIG["INPUT_SUFFIX"]
OUTPUT_LABEL = CONFIG["OUTPUT_SUFFIX"]
META_LABEL = CONFIG["METADATA_SUFFIX"]


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
    file_name = str(pathlib.Path(src_name).name).replace(".py", "")
    cwd = pathlib.Path().cwd()
    test_save_path = pathlib.Path(cwd, "tests", SAVE_DIR, file_name)
    typer.echo(test_save_path)
    pathlib.Path(test_save_path).mkdir(parents=True, exist_ok=True)
    return test_save_path

    # make this windows and unix compatible


def cache_writer(
    f_path: str,
    obj_name: str,
    role_label: str,
    cache_data: Union[str, tuple],
    meta_mode: Optional[bool] = False,
):
    if meta_mode:
        # need to figure out how to do everything path related with pathlib
        f_name = f"{obj_name}{role_label}.json"
        save_path = pathlib.Path(f_path, f_name)
        typer.echo(f"{save_path} {pathlib.Path(save_path).exists()}")
        if not pathlib.Path(save_path).exists():
            with open(save_path, "w", encoding="utf-8") as cache:
                json.dump(cache_data, cache, indent=4)
        return save_path
    else:
        t_stamp = str(timestamp()[1]).replace(".", "-")
        f_name = f"{t_stamp}_{obj_name}{role_label}.pickle"
        save_path = pathlib.Path(f_path, f_name)
        with open(save_path, "wb") as cache:
            pickle.dump(cache_data, cache)
        return save_path

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
            path_str = path_handler_for_tests(src_file)
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
                input_fname = cache_writer(
                    path_str, obj_name, INPUT_LABEL, (args, kwargs)
                )
                typer.echo(input_fname)
                ret_value = func(*args, **kwargs)
                output_fname = cache_writer(
                    path_str,
                    obj_name,
                    OUTPUT_LABEL,
                    ret_value)
                typer.echo(output_fname)
                ts_tup = timestamp()

                metadata = {
                    "name": obj_name,
                    "timestamp_unix": ts_tup[1],
                    "timestamp_human": ts_tup[0],
                    "": "",
                }

                meta_fname = cache_writer(
                    path_str, obj_name, META_LABEL, metadata, meta_mode=True
                )
                typer.echo(meta_fname)
                return ret_value
        else:
            ret_value = func(*args, **kwargs)
            return ret_value

    return wrapper_fetcher
