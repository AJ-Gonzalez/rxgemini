"""Injection module for RX Gemini"""

# pylint: skip-file
# Skipping file because it has a pending refactor
import functools
import inspect
import pathlib

import typer


from rxgemini.configurator import config_checker

CONFIG = config_checker(internal=True)
META_LABEL = CONFIG["META_LABEL"]


def path_handler_for_tests():
    return 1


def metadata_reader(filename: str):
    typer.echo(filename)
    return {"IN": "", "OUT": ""}


def pickle_reader(filename: str):
    typer.echo(filename)


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
                        exit()
                    line = line.replace("from", "")
                    line = line.replace(lookup_val, "")
                    line = line.replace("import", "")
                    line = line.strip()
                    line = line.replace(".", "/")
                    src_path = line
        cwd = pathlib.Path.cwd()
        obj_path = src_path.replace()
        typer.echo(cwd)
        checker = path_handler_for_tests()
        typer.echo(f"fetching from{ obj_path}")
        # metadata path will need refactoring to work on windows hosts
        metadata = metadata_reader(f"{checker}/{lookup_val}{META_LABEL}.json")
        test_data = {
            "in": pickle_reader(metadata["IN"]),
            "out": pickle_reader(metadata["OUT"]),
        }
        try:
            func(args[0], test_data)
        except IndexError as err_msg:
            typer.echo(err_msg)
            func(test_data)
