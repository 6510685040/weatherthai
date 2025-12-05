import typer
from weatherthai.commands.forecast import forecast

app = typer.Typer(help="weatherthai - Thailand weather CLI")

app.command()(forecast)

if __name__ == "__main__":
    app()

print(">>> Running main.py from:", __file__)
