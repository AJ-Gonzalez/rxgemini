"""Log Handling and pront utilities"""


import logging
from logging.config import dictConfig
from datetime import datetime
from typing import Any
import coloredlogs

import typer
from rich import print as pprint

from rxgemini.configurator import config_checker
from rxgemini.constants import LOG_CONF, LOGGING_OPTS
from rxgemini.errors import ErroneousConfigError
from rxgemini import styles


dictConfig(LOG_CONF)

logger = logging.getLogger()
coloredlogs.install(logger=logger)

CONFIG = config_checker(internal=True)


try:
    PREFIX = CONFIG["LOG_PREFIX"]
    LOG_MODE = CONFIG["LOG_MODE"]
except KeyError as exc:
    raise ErroneousConfigError from exc

# Pre check of config
if LOG_MODE not in LOGGING_OPTS:
    raise ErroneousConfigError


def timestamp() -> str:
    """
    Provides formatted timestamp

    Returns:
        str: Human readable
    """
    t_stamp = datetime.now()
    human_readable: str = str(t_stamp).split(".", maxsplit=1)[0]
    return human_readable


def pretty_print(item: Any):
    """

    Pretty printer shourcut to standardize module use

    Args:
        item (Any): item to pretty print_
    """
    pprint(item)


def log_info(message: str):
    """
    Logs info message

    Args:
        message (str): message to log
    """
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.info("%s %s", PREFIX, message)
    elif LOG_MODE == LOGGING_OPTS[1]:
        typer.echo(styles.green_bold(message))
    elif LOG_MODE == LOGGING_OPTS[2]:
        message = f"{timestamp()}  {message}"
        typer.echo(styles.green_bold(message))


def general(message: str):
    """
    Logs general message

    Args:
        message (str): message to log
    """
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.info("%s %s", PREFIX, message)
    elif LOG_MODE == LOGGING_OPTS[1]:
        typer.echo(styles.cyan_bold(message))
    elif LOG_MODE == LOGGING_OPTS[2]:
        message = f"{timestamp()}  {message}"
        typer.echo(styles.cyan_bold(message))
    else:
        typer.echo(styles.cyan_bold(message))


def log_warning(message: str):
    """
    Logs warning message

    Args:
        message (str): message to log
    """
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.warning("%s %s", PREFIX, message)
    elif LOG_MODE == LOGGING_OPTS[1]:
        typer.echo(styles.yellow_bold(message))
    elif LOG_MODE == LOGGING_OPTS[2]:
        message = f"{timestamp()}  {message}"
        typer.echo(styles.yellow_bold(message))
    else:
        typer.echo(styles.yellow_bold(message))


def log_error(message: str):
    """
    Logs error message

    Args:
        message (str): message to log
    """
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.error("%s %s", PREFIX, message)
    elif LOG_MODE == LOGGING_OPTS[1]:
        typer.echo(styles.red_bold(message))
    elif LOG_MODE == LOGGING_OPTS[2]:
        message = f"{timestamp()}  {message}"
        typer.echo(styles.red_bold(message))
    else:
        typer.echo(styles.red_bold(message))


def log_critical(message: str):
    """
    Logs critical message

    Args:
        message (str): message to log
    """
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.critical("%s %s", PREFIX, message)
    elif LOG_MODE == LOGGING_OPTS[1]:
        message = f"!!! -> {message}"
        typer.echo(styles.red_bold(message))
    elif LOG_MODE == LOGGING_OPTS[2]:
        message = f"{timestamp()} !!! -> {message}"
        typer.echo(styles.red_bold(message))
    else:
        message = f"!!! -> {message}"
        typer.echo(styles.red_bold(message))

# Syntax example
# general("sample message")
# log_info("sample message")
# log_warning("sample message")
# log_error("sample message")
# log_critical("sample message")
