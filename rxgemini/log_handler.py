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

logger.info('often makes a very good meal of %s', 'visiting tourists')
logger.error('often makes a very good meal of %s', 'visiting tourists')
logger.warning('often makes a very good meal of %s', 'visiting tourists')
logger.critical('often makes a very good meal of %s', 'visiting tourists')
logger.debug("message")

CONFIG = config_checker(internal=True)

PREFIX = CONFIG["LOG_PREFIX"]


def pretty_print(item: Any):
    """

    Pretty printer shourcut to standardize module use

    Args:
        item (Any): item to pretty print_
    """
    pprint(item)
