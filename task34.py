import tkinter as tk
from tkinter import messagebox

def show_help(event=None):
    messagebox.showinfo("Help", "F1 pressed! Here's your help.")

root = tk.Tk()
root.title("F1 Help Popup")
root.bind("<F1>", show_help)
root.mainloop()
