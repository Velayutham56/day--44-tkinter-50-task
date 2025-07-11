import tkinter as tk

def save_action(event=None):
    print("Saving your data...")

root = tk.Tk()
root.title("Ctrl+S Save")
root.bind("<Control-s>", save_action)
root.mainloop()
