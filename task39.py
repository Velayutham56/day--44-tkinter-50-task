import tkinter as tk

class SearchBox(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Search", command=self.search)
        self.entry.pack(side="left", fill="x", expand=True)
        self.button.pack(side="left")

    def search(self):
        print(f"Searching for: {self.entry.get()}")
