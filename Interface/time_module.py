from datetime import datetime
import tkinter as tk

def create_time_label(parent):
    label = tk.Label(parent, fg="white", bg="black", font=("Helvetica", 28, "bold"))
    label.pack(side="left", padx=20)

    def update_time():
        now = datetime.now().strftime("%I:%M:%S %p")
        label.config(text=now)
        label.after(1000, update_time)

    update_time()
    return label