import tkinter as tk

class ButtonPair(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        tk.Button(self, text="OK", command=self.ok).pack(side="left")
        tk.Button(self, text="Cancel", command=self.cancel).pack(side="left")

    def ok(self):
        print("OK clicked")

    def cancel(self):
        print("Cancel clicked")
