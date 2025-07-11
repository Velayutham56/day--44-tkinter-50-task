import tkinter as tk

def auto_cap(event):
    entry.insert(tk.END, event.char.upper())
    return "break"  # prevent default insert

root = tk.Tk()
root.title("Auto-Capitalize Entry")
entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Key>", auto_cap)

root.mainloop()
