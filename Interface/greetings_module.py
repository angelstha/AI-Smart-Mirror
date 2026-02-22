import tkinter as tk

def create_greeting_ticker(parent):
    label = tk.Label(parent, fg="cyan", bg="black", font=("Helvetica", 24, "bold"))
    label.place(x=parent.winfo_width(), y=5)

    x_pos = parent.winfo_width()

    def slide_text():
        nonlocal x_pos
        x_pos -= 2  # speed of sliding
        label.place(x=x_pos, y=5)

        if x_pos < -label.winfo_reqwidth():
            x_pos = parent.winfo_width()

        label.after(30, slide_text)

    def show_greeting(text):
        label.config(text=text)
        nonlocal x_pos
        x_pos = parent.winfo_width()  # reset position when new greeting appears

    slide_text()
    return show_greeting