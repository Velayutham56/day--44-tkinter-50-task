import tkinter as tk

def close_app(event):
    root.destroy()

root = tk.Tk()
root.title("Press Esc to Exit")
root.bind("<Escape>", close_app)
root.mainloop()
