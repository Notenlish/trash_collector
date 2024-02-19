from rich import print, color, emoji, tree, spinner, status, progress_bar, live
from rich.console import Console
from rich.table import Table

console = Console()

import typer

from typing import Optional
from typing_extensions import Annotated
from search import start_search

# cli arg = req.
# cli options = not req.

# ✨✨✨✨✨


def main(
    search: Annotated[
        Optional[bool],
        typer.Option(
            "--search",
            "-s",
            case_sensitive=False,
            help="Determines if it should search.",
        ),
    ] = None,
    start_dir: Annotated[
        Optional[str],
        typer.Option(
            "--start-dir", "-d", help="Defines the Directory for starting search"
        ),
    ] = ".",
    max_depth: Annotated[
        Optional[int],
        typer.Option("--max-depth", "-md", help="Max depth for search"),
    ] = -1,
):
    """ """
    if search in [None, "--search", "-s"]:
        search = True
    if search:
        start_search(start_dir, max_depth)
