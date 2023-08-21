"""Log Handling and pront utilities"""


import logging
from logging.config import dictConfig
from typing import Any
import coloredlogs

from rich import print as pprint

from rxgemini.configurator import config_checker
from rxgemini.constants import LOG_CONF


dictConfig(LOG_CONF)

logger = logging.getLogger()
coloredlogs.install(logger=logger)

CONFIG = config_checker(internal=True)

PREFIX = CONFIG["LOG_PREFIX"]


def pretty_print(item: Any):
    """

    Pretty printer shourcut to standardize module use

    Args:
        item (Any): item to pretty print_
    """
    pprint(item)


def info(message: str):
    logger.info("%s %s", PREFIX, message)


def warning(message: str):
    logger.warning("%s %s", PREFIX, message)


def error(message: str):
    logger.error("%s %s", PREFIX, message)


def critical(message: str):
    logger.critical("%s %s", PREFIX, message)




critical("sample message")
