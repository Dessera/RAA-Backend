from typer import Typer, Option
import uvicorn
from .. import app

subcommand = Typer()


@subcommand.command(help="运行服务器")
def run(
    host: str = Option("127.0.0.1", help="运行服务器的主机地址"),
    port: int = Option(8000, help="运行服务器的端口号"),
):
    uvicorn.run(app, host=host, port=port)
