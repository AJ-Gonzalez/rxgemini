"""Configuration Handler module for RX Gemini"""
from pathlib import Path

import yaml
import typer

from rxgemini import styles


CFG_NAME: tuple = ("rxgemini_cfg.yaml", "rxgemini_cfg.yml")

CFG_TEMPLATE: dict = {"FORMALITY": 0, "METADATA_SUFFIX": "-meta", "": ""}


def config_checker():
    print(Path().cwd())
    for f_name in CFG_NAME:
        # Instantiate the Path class
        obj = Path(f_name)

        # Check if path exists
        msg = f"{obj.exists()} {f_name}"
        typer.echo(styles.cyan_bold(msg))
