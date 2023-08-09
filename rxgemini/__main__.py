"""Main entrypoint module for RX Gemini CLI"""

import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def example():
    """
    Sample Command
    """
    typer.echo("example")


if __name__ == "__main__":
    app()
