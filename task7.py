import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hover over me", fg="black", bg="white")
label.pack()

def on_enter(e):
    label.config(fg="red")

def on_leave(e):
    label.config(fg="black")

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

root.mainloop()
