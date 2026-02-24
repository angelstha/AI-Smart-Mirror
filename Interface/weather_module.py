import tkinter as tk
import requests

API_KEY = "fcdd6b9a5ded1a0d458bc027f0641a72"
CITY = "Kathmandu"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        temp = round(data["main"]["temp"])
        condition = data["weather"][0]["description"].capitalize()
        return f"{temp}°C {condition}"
    except Exception:
        return "Weather unavailable"

def create_weather_label(parent):
    frame = tk.Frame(parent, bg="black")
    frame.pack(side="right", padx=20)

    weather_text = get_weather()
    weather_label = tk.Label(frame, text=weather_text, fg="white", bg="black", font=("Helvetica", 22))
    weather_label.pack(side="left")

    nice_day_label = tk.Label(frame, text="Have a nice day!", fg="white", bg="black", font=("Helvetica", 16, "italic"))
    nice_day_label.pack(side="left", padx=10)

    return frame
