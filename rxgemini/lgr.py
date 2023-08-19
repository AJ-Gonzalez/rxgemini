"""Log Handling and output syling, abbreviated from logger to lgr"""

from typing import Any

import typer

from rich import print as pprint


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


if __name__ == "__main__":
    typer.echo(green_bold("example text here"))
    typer.echo(red_bold("more sample text"))
    typer.echo(yellow_bold("more sample text"))


def pretty_print(item: Any):
    """

    Pretty printer shourcut to standardize module use

    Args:
        item (Any): item to pretty print_
    """
    pprint(item)
