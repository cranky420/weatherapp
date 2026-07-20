from pathlib import Path

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Weather Platform API",
    description="A production-ready weather platform built with FastAPI.",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


@app.get("/")
def root():
    return FileResponse(BASE_DIR / "static" / "index.html")


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/weather")
def weather(city: str = "Kolkata"):
    try:
        geocoding_response = httpx.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
            timeout=10.0,
        )
        geocoding_response.raise_for_status()
        geocoding_data = geocoding_response.json()

        if not geocoding_data.get("results"):
            return {
                "city": city,
                "error": "City not found",
            }

        location = geocoding_data["results"][0]

        lat = location["latitude"]
        lon = location["longitude"]

        forecast_response = httpx.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,pressure_msl,weather_code",
                "timezone": "auto",
            },
            timeout=10.0,
        )
        forecast_response.raise_for_status()

        forecast_data = forecast_response.json()

        current = forecast_data.get("current", {})

        weather_code = int(current.get("weather_code", 0))

        return {
            "city": location.get("name", city),
            "temperature": round(current.get("temperature_2m", 0)),
            "feels_like": round(current.get("apparent_temperature", 0)),
            "condition": get_weather_condition(weather_code),
            "humidity": int(current.get("relative_humidity_2m", 0)),
            "wind": round(current.get("wind_speed_10m", 0)),
            "pressure": int(current.get("pressure_msl", 0)),
        }

    except httpx.HTTPError:
        return {
            "city": city,
            "error": "Unable to fetch weather data right now",
        }


def get_weather_condition(weather_code: int) -> str:
    mapping = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Heavy rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
    }

    return mapping.get(weather_code, "Unknown")