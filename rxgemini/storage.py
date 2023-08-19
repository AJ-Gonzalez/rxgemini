"""Storage handler for RX Gemini"""

from dataclasses import dataclass
from typing import Any


@dataclass
class LoggedInstance:
    """
    Custom Datatype to handle method/fucntion
    data and metadata.

    Gives a faithful snapshot of captured data
    as well as annotations for checking types.
    """
    obj_name: str
    timestamp_unix: float
    timestamp_human: str
    file: str
    file_path_parts: list
    docstring: str
    arg_dict: dict
    kwarg_dict: dict
    out_dict: dict
    call_contents: list
    return_content: Any
