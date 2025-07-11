import tkinter as tk

class ToolBar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.make_button("Open", self.open)
        self.make_button("Save", self.save)
        self.make_button("Exit", self.exit)

    def make_button(self, name, cmd):
        tk.Button(self, text=name, command=cmd).pack(side="left")

    def open(self): print("Open clicked")
    def save(self): print("Save clicked")
    def exit(self): self.master.destroy()
