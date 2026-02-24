import tkinter as tk
from time_module import create_time_label
from weather_module import create_weather_label
from greetings_module import create_greeting_ticker
from calendar_module import create_calendar
from reminders_module import create_reminders
from face_module import detect_and_recognize, load_known_faces
import cv2
from PIL import Image, ImageTk
import threading
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="face_recognition_models")

# --- Root Window ---
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

# --- Camera Feed inside Tkinter ---
video_label = tk.Label(root, bg="black")
video_label.pack(side="left", padx=20, pady=20)

known_encodings, known_names = load_known_faces("known_faces")
video_capture = cv2.VideoCapture(0)

def update_frame():
    ret, frame = video_capture.read()
    if ret:
        # Detect faces
        faces = detect_and_recognize(frame, known_encodings, known_names)
        if faces:
            for (_, _, _, _, name) in faces:
                show_greeting(f"Hello {name}!")
                show_greeting("Love the outfit!")
                show_greeting("Have a nice day!")
        else:
            show_greeting("Hello Guest!")

        # Convert frame to Tkinter image
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.config(image=imgtk)

    video_label.after(30, update_frame)

# Start updating frames
update_frame()

# --- Start Tkinter main loop ---
root.mainloop()