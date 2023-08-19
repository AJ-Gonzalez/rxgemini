"""Main entrypoint module for RX Gemini CLI"""

import sys

import typer

from rxgemini import lgr
from rxgemini import configurator
from rxgemini import constants


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
    typer.echo(constants.DESCRIPTION)


@app.command()
def generate_config():
    """
    Checks if there is a configuration file and generates one if there
    is none
    """
    typer.echo(lgr.cyan_bold("Checking for configuration file..."))
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
    typer.echo(lgr.cyan_bold("WIP Placeholder for test generator"))


if __name__ == "__main__":
    app()
