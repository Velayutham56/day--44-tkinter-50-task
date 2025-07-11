import tkinter as tk

class LabelButton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label = tk.Label(self, text="Hello!")
        self.button = tk.Button(self, text="Click", command=self.say_hello)
        self.label.pack()
        self.button.pack()

    def say_hello(self):
        self.label.config(text="Button clicked!")
