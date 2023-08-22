"""Log Handling and output syling, abbreviated from logger to lgr"""

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
