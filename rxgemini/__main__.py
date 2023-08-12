"""Main entrypoint module for RX Gemini CLI"""

import sys

import typer

from rxgemini import styles
from rxgemini import configurator


app = typer.Typer()


@app.callback()
def callback():
    """
    RX Gemini:


    Python unit test automation toolkit.
    Generate real-world faithful unit tests with zero overhead.

    RX Gemini empowers developers, testers, and management
    to focus on features and code quality.


    """


@app.command()
def about():
    """
    About RX Gemini and Licensing
    """
    description: str = """
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
    typer.echo(description)


@app.command()
def generate_config():
    """
    Checks if there is a configuration file and generates one if there
    is none
    """
    typer.echo(styles.cyan_bold("Checking for configuration file..."))
    if configurator.config_checker():
        sys.exit()
    else:
        typer.echo("Writing configuration...")
        configurator.config_writer()


@app.command()
def generate_tests():
    """
    Sample Command
    """
    typer.echo(styles.cyan_bold("WIP Placeholder for test generator"))


if __name__ == "__main__":
    app()
