"""Module for libary-wide constants"""


CFG_NAME: tuple = ("rxgemini_cfg.yaml", "rxgemini_cfg.yml")

CFG_TEMPLATE: dict = {
    "FORMALITY": 0,
    "METADATA_SUFFIX": "-meta",
    "INPUT_SUFFIX": "-input",
    "OUTPUT_SUFFIX": "-output",
    "MARKER_KW": "RXGEMINI",
    "TAGS": {"FETCHER": ["fetcher", "on", "off"]},
    "DELIMITERS": ["_about_", "_regarding_", "_evaluates_", "_ensures_"],
    "LOG_PREFIX": "[RX_GEMINI]",
    "SAVE_DIRECTORY": "test_dc",
}


DESCRIPTION: str = """
    RX Gemini: Python unit test automation toolkit
    Copyright (C) 2023  AJ Gonzalez

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    """
