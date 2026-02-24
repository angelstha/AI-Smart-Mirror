import tkinter as tk
from datetime import datetime
import calendar

root = tk.Tk()
root.title("Smart Mirror UI")
root.geometry("1000x700")
root.configure(bg="black")

# --- Top Bar ---
top_frame = tk.Frame(root, bg="black", height=60)
top_frame.pack(side="top", fill="x", pady=10)

time_label = tk.Label(top_frame, fg="white", bg="black", font=("Helvetica", 24))
time_label.pack(side="left", padx=20)

# Greeting ticker
greet_frame = tk.Frame(top_frame, bg="black", height=40)
greet_frame.pack(side="left", expand=True, fill="x")

greeting_label = tk.Label(greet_frame, fg="cyan", bg="black", font=("Helvetica", 22, "bold"))
greeting_label.place(x=greet_frame.winfo_width(), y=5)

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

# Calendar grid
cal_frame = tk.Frame(right_frame, bg="black")
cal_frame.pack(pady=10)

# Reminders dictionary (month-day only)
reminders = {
    "02-25": "Doctor Appointment",
    "02-28": "Project Deadline",
    "03-02": "Dinner with Friends"
}

# --- Calendar Display with Highlights ---
def show_calendar(year, month):
    # Clear old widgets
    for widget in cal_frame.winfo_children():
        widget.destroy()

    month_name = calendar.month_name[month]
    header = tk.Label(cal_frame, text=f"{month_name} {year}", fg="white", bg="black", font=("Helvetica", 16, "bold"))
    header.grid(row=0, column=0, columnspan=7, pady=5)

    # Weekday headers
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days):
        tk.Label(cal_frame, text=day, fg="white", bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=i, padx=5, pady=5)

    # Calendar days
    cal = calendar.monthcalendar(year, month)
    for r, week in enumerate(cal, start=2):
        for c, day in enumerate(week):
            if day == 0:
                tk.Label(cal_frame, text=" ", bg="black", width=4).grid(row=r, column=c)
            else:
                date_key = f"{month:02d}-{day:02d}"
                if date_key in reminders:
                    tk.Label(cal_frame, text=str(day), bg="#a8dadc", fg="black", width=4, font=("Helvetica", 12, "bold")).grid(row=r, column=c, padx=2, pady=2)
                else:
                    tk.Label(cal_frame, text=str(day), bg="black", fg="white", width=4, font=("Helvetica", 12)).grid(row=r, column=c, padx=2, pady=2)

    # Update reminder list
    reminder_list.delete(0, tk.END)
    for date, task in reminders.items():
        reminder_list.insert(tk.END, f"{date}: {task}")

# Reminder list
reminder_label = tk.Label(right_frame, text="Reminders:", fg="yellow", bg="black", font=("Helvetica", 16, "bold"))
reminder_label.pack(pady=5)

reminder_list = tk.Listbox(right_frame, width=25, height=5, bg="black", fg="white", font=("Helvetica", 14))
reminder_list.pack()

# Show current month
today = datetime.today()
show_calendar(today.year, today.month)

root.mainloop()