from fastapi import APIRouter
import requests
from ..database import engine, weather_table

router = APIRouter()


@router.post("/ingest-weather")
def ingest_weather():

    API_KEY = "fe3928efb2761e86001921773d9332e4"
    city = "Lahore"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch weather data"}

    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    conn = engine.connect()

    conn.execute(
        weather_table.insert().values(
            city=city,
            temperature=str(temperature),
            description=description
        )
    )

    conn.commit()
    conn.close()

    return {
        "message": "Weather data ingested successfully",
        "city": city,
        "temperature": temperature,
        "description": description
    }


@router.get("/weather-data")
def get_weather_data():

    conn = engine.connect()

    result = conn.execute(weather_table.select()).fetchall()

    conn.close()

    return [dict(row._mapping) for row in result]