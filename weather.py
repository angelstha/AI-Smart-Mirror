import requests
import time

# Insert your real OpenWeatherMap API key here
API_KEY = "fcdd6b9a5ded1a0d458bc027f0641a72"

_last_weather = None
_last_update = 0

def get_weather(city="Kathmandu", api_key=API_KEY, refresh_interval=600):
    """
    Fetch weather info from OpenWeatherMap.
    Caches results for 'refresh_interval' seconds (default 10 minutes).
    """
    global _last_weather, _last_update
    now = time.time()

    # Use cached result if still fresh
    if _last_weather and (now - _last_update) < refresh_interval:
        return _last_weather

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("main"):
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"].capitalize()
            #  Use chr(176) for degree symbol to avoid "??"
            _last_weather = f"{city}: {temp}{chr(176)}C, {condition}"
        else:
            _last_weather = "Weather data unavailable"
    except Exception as e:
        _last_weather = f"Weather error: {e}"

    _last_update = now
    return _last_weather
