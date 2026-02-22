import tkinter as tk
from time_module import create_time_label
from weather_module import create_weather_label
from greetings_module import create_greeting_ticker
from calendar_module import create_calendar
from reminders_module import create_reminders
from face_module import run_face_detection, load_known_faces
import threading

root = tk.Tk()
root.title("Smart Mirror UI")
root.geometry("1200x800")
root.configure(bg="black")

# --- Top Bar ---
top_frame = tk.Frame(root, bg="black", height=80)
top_frame.pack(side="top", fill="x", pady=10)

create_time_label(top_frame)

greet_frame = tk.Frame(top_frame, bg="black", height=40)
greet_frame.pack(side="left", expand=True, fill="x")
show_greeting = create_greeting_ticker(greet_frame)

create_weather_label(top_frame)

# --- Right Column ---
right_frame = tk.Frame(root, bg="black")
right_frame.pack(side="right", fill="y", padx=20, pady=20)

reminders = {
    "02-25": "Doctor Appointment",
    "02-28": "Project Deadline",
    "03-02": "Dinner with Friends"
}

create_calendar(right_frame, reminders)
create_reminders(right_frame, reminders)

# --- Face