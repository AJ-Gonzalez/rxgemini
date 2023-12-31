"""Storage handler for RX Gemini"""

import pickle
import pathlib

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from rxgemini.configurator import config_checker
from rxgemini.constants import EXT
from rxgemini.log_handler import log_info
from rxgemini.cls_tools import index_finder

CONFIG = config_checker(internal=True)

SAVE_DIR = CONFIG["SAVE_DIRECTORY"]


@dataclass
class LoggedInstance:
    """
    Custom Datatype to handle method/fucntion
    data and metadata.

    Gives a faithful snapshot of captured data
    as well as annotations for checking types.
    """
    # pylint: disable=too-many-instance-attributes
    # Number of attributes being large is preferable
    # To having too many metadata files per call.
    obj_name: str
    timestamp_unix: float
    timestamp_human: str
    caller: str
    file: str
    file_path_parts: list
    docstring: str
    expected_types: dict
    actual_types: dict
    call_contents: dict
    return_content: Any


def get_relative_path(absolute_path: str) -> pathlib.Path:
    """
    Gets relative path from CWD

    Args:
        absolute_path (str): Absolute path

    Returns:
        pathlib.Path: relative path object
    """
    cwd = pathlib.Path().cwd()
    return pathlib.Path(absolute_path).relative_to(cwd)


def path_handler(src_name: str) -> pathlib.Path:
    """
    Handles paths for call storage

    Args:
        src_name (str): source file

    Returns:
        pathlib.Path: save path for file
    """
    file_name = str(pathlib.Path(src_name).name).replace(".py", "")
    cwd = pathlib.Path().cwd()
    test_save_path = pathlib.Path(cwd, "test", SAVE_DIR, file_name)
    log_info(f"Save path is: {test_save_path}")
    pathlib.Path(test_save_path).mkdir(parents=True, exist_ok=True)
    return test_save_path


def timestamp() -> tuple:
    """
    Provides formatted timestamps for metadata.

    Returns:
        tuple: Human readable, unix format
    """
    t_stamp = datetime.now()
    human_readable: str = str(t_stamp).split(".", maxsplit=1)[0]
    unix_readable: float = t_stamp.timestamp()
    return (human_readable, unix_readable)


def store_instance(instance: LoggedInstance) -> str:
    """
    Stores data for call or instance of func/method in a
    .gmni file.

    Takes the LoggedInstance object and dumps it into
    a binary file using pickle.

    Args:
        instance (LoggedInstance): Logged call of method/func

    Returns:
        str: Path where file was saved
    """
    t_stamp = str(timestamp()[1]).replace(".", "-")
    cmp_idx: int = index_finder(instance.call_contents)
    f_name = f"{cmp_idx}+{t_stamp}{instance.obj_name}{EXT}"
    print(f_name)
    save_path = pathlib.Path(*instance.file_path_parts, f_name)
    with open(save_path, "wb") as file_data:
        pickle.dump(instance, file_data)
    return str(save_path)
