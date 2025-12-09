import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5"


def _require_api_key():
    if not API_KEY:
        raise RuntimeError("❌ OPENWEATHER_API_KEY is not set in environment or .env file")


def get_forecast(city: str):
    """ดึงพยากรณ์อากาศ 5 วัน / 3 ชั่วโมง จาก OpenWeather"""
    _require_api_key()

    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "th",
    }

    resp = requests.get(url, params=params, timeout=10)

    if resp.status_code != 200:
        try:
            data = resp.json()
            message = data.get("message", resp.text)
        except Exception:
            message = resp.text

        raise RuntimeError(f"❌ ไม่สามารถดึงพยากรณ์อากาศของเมือง '{city}' ได้: {message}")

    return resp.json()

def get_current_weather(city: str):
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "th"
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Error: {response.json()}")

    return response.json()

def get_city_coordinates(city: str):
    """ดึงพิกัด lat/lon ของเมืองจาก OpenWeather"""
    _require_api_key()

    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "th"
    }

    resp = requests.get(url, params=params, timeout=10)

    if resp.status_code != 200:
        data = resp.json()
        raise RuntimeError(f"❌ ไม่พบเมือง '{city}': {data.get('message', resp.text)}")

    json_data = resp.json()
    return json_data["coord"]["lat"], json_data["coord"]["lon"]

def get_air_quality(city: str):
    """ดึงข้อมูลคุณภาพอากาศ (Air Pollution)"""
    _require_api_key()

    lat, lon = get_city_coordinates(city)

    url = f"{BASE_URL}/air_pollution"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY
    }

    resp = requests.get(url, params=params, timeout=10)

    if resp.status_code != 200:
        data = resp.json()
        raise RuntimeError(f"❌ ไม่สามารถดึงคุณภาพอากาศของ '{city}' ได้: {data.get('message', resp.text)}")

    return resp.json()