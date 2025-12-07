import typer
from weatherthai.commands.forecast import forecast_command
from weatherthai.commands.current import current_command

app = typer.Typer(help="weatherthai - Thailand weather CLI")


app.command(name="forecast")(forecast_command)
app.command(name="current")(current_command)

if __name__ == "__main__":
    app()
