import os
import requests
from dotenv import load_dotenv

load_dotenv()   # 👈 ADD THIS LINE

def get_weather(city: str) -> dict:
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return {"error": "WEATHER_API_KEY not set"}

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
