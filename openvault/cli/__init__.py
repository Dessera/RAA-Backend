from typer import Typer
from . import server_cli, databse_cli

app = Typer()


app.add_typer(server_cli.subcommand, name="server")
app.add_typer(databse_cli.subcommand, name="database")
