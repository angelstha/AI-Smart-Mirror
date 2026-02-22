import tkinter as tk

def create_reminders(parent, reminders):
    reminder_label = tk.Label(parent, text="Reminders:", fg="yellow", bg="black", font=("Helvetica", 18, "bold"))
    reminder_label.pack(pady=5)

    reminder_list = tk.Listbox(parent, width=25, height=6, bg="black", fg="white", font=("Helvetica", 16))
    reminder_list.pack()

    for date, task in reminders.items():
        reminder_list.insert(tk.END, f"{date}: {task}")

    return reminder_list