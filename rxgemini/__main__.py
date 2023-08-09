"""Main entrypoint module for RX Gemini CLI"""

import typer


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
def example():
    """
    Sample Command
    """
    typer.echo("example")


if __name__ == "__main__":
    app()
