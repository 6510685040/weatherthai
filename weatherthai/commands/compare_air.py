import typer
from weatherthai.api_client import get_air_quality

def aqi_text(aqi: int):
    return {
        1: "ดี 🙂",
        2: "พอใช้ 🙂",
        3: "ปานกลาง 😐",
        4: "แย่ 😷",
        5: "อันตราย ☠️"
    }.get(aqi, "ไม่ทราบ")

def compare_air_command(
    city1: str = typer.Argument(..., help="เมืองที่ 1"),
    city2: str = typer.Argument(..., help="เมืองที่ 2"),
):
    """เปรียบเทียบคุณภาพอากาศของสองเมือง"""

    data1 = get_air_quality(city1)
    data2 = get_air_quality(city2)

    info1 = data1["list"][0]
    info2 = data2["list"][0]

    aqi1 = info1["main"]["aqi"]
    aqi2 = info2["main"]["aqi"]

    pm25_1 = info1["components"]["pm2_5"]
    pm25_2 = info2["components"]["pm2_5"]

    typer.echo(f"📍 {city1}")
    typer.echo(f"  - AQI: {aqi1} ({aqi_text(aqi1)})")
    typer.echo(f"  - PM2.5: {pm25_1} µg/m³\n")

    typer.echo(f"📍 {city2}")
    typer.echo(f"  - AQI: {aqi2} ({aqi_text(aqi2)})")
    typer.echo(f"  - PM2.5: {pm25_2} µg/m³\n")

    if pm25_1 < pm25_2:
        typer.echo(f"✅ อากาศดีกว่า: {city1}")
    elif pm25_2 < pm25_1:
        typer.echo(f"✅ อากาศดีกว่า: {city2}")
    else:
        typer.echo("⚖️ คุณภาพอากาศใกล้เคียงกัน")
