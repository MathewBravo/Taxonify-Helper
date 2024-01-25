import typer
import file_operations

from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def treeify(filename: str, output_filename: Annotated[Optional[str], typer.Argument()] = None):
    file_operations.open_config("tree", filename, output_filename)
