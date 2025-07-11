import tkinter as tk

class LiveEntryLabel(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label = tk.Label(self, text="")
        self.entry = tk.Entry(self)
        self.entry.bind("<KeyRelease>", self.update_label)
        self.label.pack()
        self.entry.pack()

    def update_label(self, event):
        self.label.config(text=self.entry.get())
