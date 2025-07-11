import tkinter as tk

root = tk.Tk()

def change_text(event):
    label.config(text="Text Changed!")

label = tk.Label(root, text="Double Click Me")
label.bind("<Double-Button-1>", change_text)
label.pack()

root.mainloop()
