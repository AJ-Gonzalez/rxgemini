"""Injection module for RX Gemini"""

import functools
import inspect
import pathlib
import sys

import typer


from rxgemini.configurator import config_checker
from rxgemini.log_handler import log_warning, log_info
from rxgemini.constants import EXT

CONFIG = config_checker(internal=True)
SAVE_DIR = CONFIG["SAVE_DIRECTORY"]


def path_handler_for_tests():
    return 1


def metadata_reader(filename: str):
    log_info(filename)
    return {"IN": "", "OUT": ""}


def pickle_reader(filename: str):
    log_info(filename)


def retrive_test_data(method_identifier: str):
    log_info(f"Gathering data for {method_identifier} tests")
    data_path = pathlib.Path().joinpath(SAVE_DIR, method_identifier)
    data_files = [f for f in data_path.glob(f"*{EXT}")]
    log_info(f"Found {data_files} data points.")


# This is for next ticket, ignore for now
def auto_injector(func):
    @functools.wraps(func)
    def wrapper_injector(*args):
        # THis whole fucntion will be refactored later
        obj_name = func.__name__
        obj_file = inspect.getfile(func)
        lookup_val = obj_name.replace("test_", "")
        src_path = ""
        with open(obj_file, "r", encoding="utf-8") as src_file:
            for line in src_file:
                if "import" in line and lookup_val in line:
                    # may add support for comma imports and import ()
                    if "," in line:
                        typer.echo("error")
                        sys.exit()
                    line = line.replace("from", "")
                    line = line.replace(lookup_val, "")
                    line = line.replace("import", "")
                    line = line.strip()
                    line = line.replace(".", "/")
                    src_path = line
        cwd = pathlib.Path.cwd()
        obj_path = src_path.replace()
        log_info(f"Current working directory: {cwd}")
        checker = path_handler_for_tests()
        log_info(f"Fetching from{ obj_path}")
        # metadata path will need refactoring to work on windows hosts
        metadata = metadata_reader(f"{checker}/{lookup_val}META.json")
        test_data = {
            "in": pickle_reader(metadata["IN"]),
            "out": pickle_reader(metadata["OUT"]),
        }
        try:
            func(args[0], test_data)
        except IndexError as err_msg:
            log_warning(f"Running from outside testing files:{err_msg}")
            func(test_data)
