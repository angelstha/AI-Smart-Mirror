import tkinter as tk

def create_greeting_ticker(parent):
    label = tk.Label(parent, fg="cyan", bg="black", font=("Helvetica", 24, "bold"))
    label.pack()

    messages = []
    current_index = 0
    x_pos = parent.winfo_width()
    sliding = False

    def slide_text():
        nonlocal x_pos, sliding
        if sliding:
            x_pos -= 2
            label.place(x=x_pos, y=5)
            if x_pos < -label.winfo_reqwidth():
                x_pos = parent.winfo_width()
                sliding = False
                show_next_message()
        label.after(30, slide_text)

    def show_next_message():
        nonlocal current_index, x_pos, sliding
        if messages:
            text = messages[current_index]
            label.config(text=text)
            x_pos = parent.winfo_width()
            label.place(x=x_pos, y=5)
            sliding = False
            current_index = (current_index + 1) % len(messages)
            # after 3 seconds, start sliding
            parent.after(3000, start_sliding)

    def start_sliding():
        nonlocal sliding
        sliding = True

    def add_message(text):
        messages.append(text)
        if len(messages) == 1:  # start cycle
            show_next_message()

    slide_text()
    return add_message
    root.mainloop()