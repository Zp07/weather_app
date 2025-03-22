import os
import requests

WEATHER_API_KEY= os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("WEATHER_API_BASE_URL")

def get_weather_city(city: str):
    ""
    if not WEATHER_API_KEY:
        raise ValueError("API KEY NOT CONFIG")
    
    url = f"{BASE_URL}?key={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else: 
        return None