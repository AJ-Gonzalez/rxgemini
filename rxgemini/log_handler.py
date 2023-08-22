"""Log Handling and pront utilities"""


import logging
from logging.config import dictConfig
from typing import Any
import coloredlogs

from rich import print as pprint

from rxgemini.configurator import config_checker
from rxgemini.constants import LOG_CONF, LOGGING_OPTS
from rxgemini.errors import ErroneousConfigError


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


def pretty_print(item: Any):
    """

    Pretty printer shourcut to standardize module use

    Args:
        item (Any): item to pretty print_
    """
    pprint(item)


def info(message: str):
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.info("%s %s", PREFIX, message)


def warning(message: str):
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.warning("%s %s", PREFIX, message)


def error(message: str):
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.error("%s %s", PREFIX, message)


def critical(message: str):
    if LOG_MODE == LOGGING_OPTS[0]:
        logger.critical("%s %s", PREFIX, message)


critical("sample message")
