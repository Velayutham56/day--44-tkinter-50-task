import tkinter as tk

class LabeledEntry(tk.Frame):
    def __init__(self, master=None, label_text="Label", entry_width=20):
        super().__init__(master)
        tk.Label(self, text=label_text, fg="blue", font=("Arial", 12)).pack(side="left")
        tk.Entry(self, width=entry_width).pack(side="left")
