"""Log Handling and output syling, abbreviated from logger to lgr"""


import logging
from logging.config import dictConfig
from typing import Any
import coloredlogs


import typer
from rich import print as pprint

from rxgemini.configurator import config_checker


logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
    },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
    },
    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)

logger = logging.getLogger()
coloredlogs.install(logger=logger)

logger.info('often makes a very good meal of %s', 'visiting tourists')

CONFIG = config_checker(internal=True)

PREFIX = CONFIG["LOG_PREFIX"]


def green_bold(text: str) -> str:
    """
    Green bold text

    Args:
        text (str): input text to format

    Returns:
        str: formatted text
    """
    return typer.style(text, fg=typer.colors.GREEN, bold=True)


def red_bold(text: str) -> str:
    """
    Red bold text

    Args:
        text (str): input text to format

    Returns:
        str: formatted text
    """
    return typer.style(text, fg=typer.colors.RED, bold=True)


def yellow_bold(text: str) -> str:
    """
    Yellow bold text

    Args:
        text (str): input text to format

    Returns:
        str: formatted text
    """
    return typer.style(text, fg=typer.colors.YELLOW, bold=True)


def cyan_bold(text: str) -> str:
    """
    Cyan bold text

    Args:
        text (str): input text to format

    Returns:
        str: formatted text
    """
    return typer.style(text, fg=typer.colors.CYAN, bold=True)


def magenta_bold(text: str) -> str:
    """
    Magenta bold text

    Args:
        text (str): input text to format

    Returns:
        str: formatted text
    """
    return typer.style(text, fg=typer.colors.MAGENTA, bold=True)


def pretty_print(item: Any):
    """

    Pretty printer shourcut to standardize module use

    Args:
        item (Any): item to pretty print_
    """
    pprint(item)
