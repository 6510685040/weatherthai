# weatherthai/cli.py
import typer
from weatherthai.commands.current import current
from weatherthai.commands.forecast import forecast

app = typer.Typer(help="weatherthai - Thailand weather CLI")

app.command()(current)
app.command()(forecast)

if __name__ == "__main__":
    app()
