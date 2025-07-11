import tkinter as tk

root = tk.Tk()

def disable_self(btn):
    btn.config(state="disabled")

button = tk.Button(root, text="Click to Disable", command=lambda: disable_self(button))
button.pack()

root.mainloop()
