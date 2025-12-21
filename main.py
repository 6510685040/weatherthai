import typer
'''from weatherthai.commands.forecast import forecast_command
from weatherthai.commands.current import current_command
from weatherthai.commands.air import air_command
from weatherthai.commands.rain import rain_command'''
from weatherthai.commands.compare_air import compare_air_command

app = typer.Typer(help="weatherthai - Thailand weather CLI")


'''app.command(name="forecast")(forecast_command)
app.command(name="current")(current_command)
app.command(name="air")(air_command)
app.command(name="rain")(rain_command)'''
app.command(name="compare-air")(compare_air_command)

if __name__ == "__main__":
    app()
