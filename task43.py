import tkinter as tk

class ColorPicker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        colors = ["red", "green", "blue", "yellow"]
        self.label = tk.Label(self, text="Choose color", bg="white", width=20)
        self.label.pack()
        for color in colors:
            tk.Button(self, bg=color, width=10, command=lambda c=color: self.pick(c)).pack(side="left")

    def pick(self, color):
        self.label.config(bg=color)
