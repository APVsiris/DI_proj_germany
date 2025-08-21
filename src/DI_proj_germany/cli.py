"""Console script for DI_proj_germany."""

import typer
from rich.console import Console

from DI_proj_germany import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for DI_proj_germany."""
    console.print("Replace this message by putting your code into "
               "DI_proj_germany.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
