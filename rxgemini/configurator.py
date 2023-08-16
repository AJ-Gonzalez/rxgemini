"""Configuration Handler module for RX Gemini"""
from pathlib import Path
from typing import Union

import yaml
import typer
from rich import print as fprint

from rxgemini import styles
from rxgemini.errors import MissingConfigError


CFG_NAME: tuple = ("rxgemini_cfg.yaml", "rxgemini_cfg.yml")

CFG_TEMPLATE: dict = {
    "FORMALITY": 0,
    "METADATA_SUFFIX": "-meta",
    "INPUT_SUFFIX": "-input",
    "OUTPUT_SUFFIX": "-output",
    "MARKER_KW": "RXGEMINI",
    "TAGS": {"FETCHER": ["fetcher", "on", "off"]},
    "DELIMITERS": ["_about_", "_regarding_", "_evaluates_"],
    "LOG_PREFIX": "[RX_GEMINI]",
    "SAVE_DIRECTORY": "test_data_cache",
}


def config_loader(filename: str) -> dict:
    """

    Loads configuration if it exists

    Args:
        filename (str): Configuration file name

    Returns:
        dict: Configuration data
    """
    try:
        with open(filename, "r", encoding="utf-8") as cfgfile:
            return yaml.safe_load(cfgfile)
    except (FileNotFoundError, PermissionError) as err:
        typer.echo(styles.red_bold(f"Error with configuration file: {err}"))
        typer.echo(styles.red_bold("File does not exist or is inaccessible"))
        return None


def config_writer():
    """
    Writes the default RX Gemini configuration file
    upon user confirmation.
    """
    write = typer.confirm(styles.cyan_bold("Generate config file?"))
    if write:
        f_name: str = CFG_NAME[0]
        typer.echo(styles.cyan_bold(f"Writing config file {f_name}"))
        with open(f_name, "w", encoding="utf-8") as cfg:
            yaml.dump(CFG_TEMPLATE, cfg)
    else:
        typer.echo(styles.yellow_bold("Operation cancelled by User."))


def config_checker(internal: bool = False) -> Union[bool, dict]:
    """
    Checks if there is a correctly formatted
    configuration file with a valil yaml
    extension in the current working directory.

    In internal mode, it will return loaded config


    Args:
        internal (bool, optional): Internal mode. Defaults to False.

    Returns:
        bool: configuration file exists
        dict: loaded config
    """
    if internal:
        for f_name in CFG_NAME:
            checker = Path(f_name)
            if checker.exists():
                return config_loader(f_name)
        raise MissingConfigError
    typer.echo(styles.magenta_bold(f"Checking directory: {Path().cwd()}"))
    for f_name in CFG_NAME:
        # Instantiate the Path class
        obj = Path(f_name)

        # Check if path exists
        if obj.exists():
            msg = f"Found configuration file: {f_name}"
            typer.echo(styles.green_bold(msg))
            fprint(config_loader(f_name))
            return True
    typer.echo(styles.yellow_bold("No configuration file found"))
    return False
