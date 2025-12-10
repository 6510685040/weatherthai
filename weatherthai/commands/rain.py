import typer
from weatherthai.api_client import get_forecast

RAIN_KEYWORDS = ["rain", "shower", "thunderstorm", "drizzle"]

def rain_command(
    city: str = typer.Option(..., help="ชื่อเมืองที่ต้องการดูความเสี่ยงฝนตก"),
    hours: int = typer.Option(6, help="จำนวนชั่วโมงถัดไป (3–24)")
):
    """ความเสี่ยงฝนตกรายชั่วโมง (ประมาณการจากข้อมูล 3 ชั่วโมง)"""

    if hours < 3 or hours > 24:
        typer.echo("❌ จำนวนชั่วโมงต้องอยู่ระหว่าง 3–24")
        return

    try:
        data = get_forecast(city)
    except Exception as e:
        typer.echo(f"❌ ดึงข้อมูลล้มเหลว: {e}")
        return

    typer.echo(f"\n🌧 ความเสี่ยงฝนตกรายชั่วโมงสำหรับ {city}\n")

    # forecast data -> list every 3 hours
    forecasts = data.get("list", [])[: hours // 3]

    for item in forecasts:
        time_txt = item["dt_txt"]
        weather_desc = item["weather"][0]["description"]
        pop = item.get("pop", 0) * 100  # probability of precipitation

        # ประเมินจาก keyword
        risk = "มีโอกาสสูง" if any(k in weather_desc.lower() for k in RAIN_KEYWORDS) else "ต่ำ"

        typer.echo(
            f"- {time_txt}: "
            f"{weather_desc} | POP: {pop:.0f}% | ความเสี่ยง: {risk}"
        )
