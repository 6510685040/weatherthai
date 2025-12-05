import typer
from .commands.forecast import forecast

app = typer.Typer(help="weatherthai - CLI สำหรับดูสภาพอากาศและคุณภาพอากาศ")

app.command()(forecast)