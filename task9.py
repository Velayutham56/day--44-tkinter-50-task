import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def toggle_widgets(event):
    selection = combo.get()
    state = "normal" if selection == "Enable" else "disabled"
    entry.config(state=state)

combo = ttk.Combobox(root, values=["Enable", "Disable"])
combo.current(1)
combo.bind("<<ComboboxSelected>>", toggle_widgets)
combo.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()
