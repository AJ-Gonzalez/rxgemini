"""Configuration Handler module for RX Gemini"""
from pathlib import Path

import yaml
import typer
from rich import print as fprint

from rxgemini import styles


CFG_NAME: tuple = ("rxgemini_cfg.yaml", "rxgemini_cfg.yml")

CFG_TEMPLATE: dict = {
    "FORMALITY": 0,
    "METADATA_SUFFIX": "-meta",
    "MARKER_KW": "RXGEMINI",
    "TAGS": {"FETCHER": ["fetcher", "on", "off"]},
    "DELIMITERS": ["_about_", "_regarding_", "_evaluates_"],
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
    pass


def config_checker():
    print(Path().cwd())
    for f_name in CFG_NAME:
        # Instantiate the Path class
        obj = Path(f_name)

        # Check if path exists
        msg = f"{obj.exists()} {f_name}"
        typer.echo(styles.cyan_bold(msg))
        fprint(config_loader(f_name))
