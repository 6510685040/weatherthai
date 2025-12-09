import typer
from weatherthai.api_client import get_air_quality

def air_command(
    city: str = typer.Option(..., help="ชื่อเมืองที่ต้องการดูคุณภาพอากาศ")
):
    """ดูคุณภาพอากาศของเมือง"""
    try:
        data = get_air_quality(city)
        aqi = data["list"][0]["main"]["aqi"]

        # ดัชนี AQI ของ OpenWeather: 1–5
        aqi_text = {
            1: "🌱 ดีมาก",
            2: "😊 ดี",
            3: "😐 ปานกลาง",
            4: "⚠️ ไม่ดี",
            5: "☠️ อันตราย"
        }

        components = data["list"][0]["components"]

        typer.echo(f"\nคุณภาพอากาศในเมือง {city}")
        typer.echo(f"ดัชนีคุณภาพอากาศ (AQI): {aqi} - {aqi_text.get(aqi, 'Unknown')}")
        typer.echo("\nมลพิษหลัก (μg/m3):")
        typer.echo(f"- PM2.5: {components['pm2_5']}")
        typer.echo(f"- PM10: {components['pm10']}")
        typer.echo(f"- O₃: {components['o3']}")
        typer.echo(f"- NO₂: {components['no2']}")
        typer.echo(f"- SO₂: {components['so2']}")
        typer.echo(f"- CO: {components['co']}")

    except Exception as e:
        typer.echo(f"❌ เกิดข้อผิดพลาด: {e}")