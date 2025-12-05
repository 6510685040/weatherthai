import typer
from weatherthai.api_client import get_forecast
from weatherthai.utils import summarize_daily_forecast


def forecast(
    city: str = typer.Option(..., help="ชื่อเมืองที่ต้องการดูพยากรณ์อากาศ"),
    days: int = typer.Option(3, help="จำนวนวันที่ต้องการพยากรณ์ (1–5)"),
):
    """ดูพยากรณ์อากาศล่วงหน้าของเมือง"""
    data = get_forecast(city)
    daily_summary = summarize_daily_forecast(data, days)

    typer.echo(f"\nพยากรณ์ {days} วันสำหรับ {city}\n")
    for line in daily_summary:
        typer.echo(line)
