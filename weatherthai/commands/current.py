import typer
from weatherthai.api_client import get_current_weather

def current_command(
    city: str = typer.Option(..., help="ชื่อเมืองที่ต้องการดูสภาพอากาศ")
):
    """ดูสภาพอากาศปัจจุบันของเมือง"""
    try:
        data = get_current_weather(city)

        typer.echo(f"🌤  สภาพอากาศปัจจุบัน: {data['name']}")
        typer.echo(f"- อุณหภูมิ: {data['main']['temp']}°C")
        typer.echo(f"- ความชื้น: {data['main']['humidity']}%")
        typer.echo(f"- สภาพท้องฟ้า: {data['weather'][0]['description']}")
        typer.echo(f"- ความเร็วลม: {data['wind']['speed']} m/s")

    except Exception as e:
        typer.echo(f"❌ เกิดข้อผิดพลาด: {e}")
