import typer
from weatherthai.api_client import get_forecast
from weatherthai.utils import summarize_daily_forecast

def summary_command(
    city: str = typer.Argument(..., help="ชื่อเมือง"),
    days: int = typer.Option(3, help="จำนวนวันที่ต้องการสรุป"),
):
    """สรุปสภาพอากาศของเมือง"""

    data = get_forecast(city)
    lines = summarize_daily_forecast(data, days)

    typer.echo(f"📊 สรุปสภาพอากาศ: {city}")
    for line in lines:
        typer.echo(f"- {line}")
