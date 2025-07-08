import requests
from weather_app.config import API_KEY, DEFAULT_UNIT

def fetch_weather(city, unit=DEFAULT_UNIT):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid={API_KEY}'
    print("Fetching from:", url)  # for debugging
    response = requests.get(url)
    return response.json()