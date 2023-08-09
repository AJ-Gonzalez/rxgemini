"""Typer Style Shortcuts"""

import typer


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


if __name__ == "__main__":
    typer.echo(green_bold("example text here"))
    typer.echo(red_bold("more sample text"))
    typer.echo(yellow_bold("more sample text"))
