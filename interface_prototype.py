import tkinter as tk
from tkinter import ttk
from datetime import datetime

root = tk.Tk()
root.title("Smart Mirror UI")
root.geometry("800x600")
root.configure(bg="black")

# --- Top Bar ---
top_frame = tk.Frame(root, bg="black")
top_frame.pack(side="top", fill="x", pady=10)

time_label = tk.Label(top_frame, fg="white", bg="black", font=("Helvetica", 24))
time_label.pack(side="left", padx=20)

greeting_label = tk.Label(top_frame, text="Hello, Angel!", fg="white", bg="black", font=("Helvetica", 18))
greeting_label.pack(side="left", padx=20)

weather_label = tk.Label(top_frame, text="☀️ 22°C", fg="white", bg="black", font=("Helvetica", 18))
weather_label.pack(side="right", padx=20)

# --- Main Section ---
main_frame = tk.Frame(root, bg="black")
main_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

face_label = tk.Label(main_frame, text="[ Face Detection Feed ]", fg="white", bg="black", font=("Helvetica", 20))
face_label.place(relx=0.5, rely=0.5, anchor="center")

# --- Right Column ---
right_frame = tk.Frame(root, bg="black")
right_frame.pack(side="right", fill="y", padx=20, pady=20)

calendar_label = tk.Label(right_frame, text="Calendar:\n- Meeting 2 PM\n- Dinner 7 PM", 
                          fg="white", bg="black", font=("Helvetica", 16), justify="left")
calendar_label.pack(pady=10)

reminder_label = tk.Label(right_frame, text="Reminders:\n- Buy groceries\n- Call Mom", 
                          fg="white", bg="black", font=("Helvetica", 16), justify="left")
reminder_label.pack(pady=10)

# --- Live Clock Update ---
def update_time():
    now = datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=now)
    root.after(1000, update_time)  # refresh every second

update_time()

root.mainloop()
