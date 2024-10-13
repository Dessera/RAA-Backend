from typer import Typer

app = Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")
