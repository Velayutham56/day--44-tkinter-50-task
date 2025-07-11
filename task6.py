import tkinter as tk

root = tk.Tk()

def enable_btn():
    button.config(state="normal")

button = tk.Button(root, text="I’ll Enable in 5 sec", state="disabled")
button.pack()

root.after(5000, enable_btn)

root.mainloop()
