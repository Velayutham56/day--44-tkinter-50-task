import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

def show_popup(event):
    messagebox.showinfo("Right Click", "You just right-clicked!")

btn = tk.Button(root, text="Right Click Me")
btn.bind("<Button-3>", show_popup)
btn.pack()

root.mainloop()
