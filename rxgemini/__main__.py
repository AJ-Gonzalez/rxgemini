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
