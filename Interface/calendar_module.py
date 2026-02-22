import tkinter as tk
import calendar
from datetime import datetime

def create_calendar(parent, reminders):
    frame = tk.Frame(parent, bg="black")
    frame.pack(pady=10)

    today = datetime.today()
    year, month = today.year, today.month

    month_name = calendar.month_name[month]
    header = tk.Label(frame, text=f"{month_name} {year}", fg="white", bg="black", font=("Helvetica", 18, "bold"))
    header.grid(row=0, column=0, columnspan=7, pady=5)

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        tk.Label(frame, text=day, fg="white", bg="black", font=("Helvetica", 14, "bold")).grid(row=1, column=i, padx=5, pady=5)

    cal = calendar.monthcalendar(year, month)
    for r, week in enumerate(cal, start=2):
        for c, day in enumerate(week):
            if day == 0:
                tk.Label(frame, text=" ", bg="black", width=4).grid(row=r, column=c)
            else:
                date_key = f"{month:02d}-{day:02d}"
                if date_key in reminders:
                    tk.Label(frame, text=str(day), bg="#a8dadc", fg="black", width=4, font=("Helvetica", 14, "bold")).grid(row=r, column=c, padx=4, pady=4)
                else:
                    tk.Label(frame, text=str(day), bg="black", fg="white", width=4, font=("Helvetica", 14)).grid(row=r, column=c, padx=4, pady=4)

    return frame