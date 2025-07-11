import tkinter as tk

class CalculatorRow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entry1 = tk.Entry(self)
        self.entry2 = tk.Entry(self)
        self.operator = tk.Label(self, text="+")
        self.result = tk.Label(self, text="Result")

        tk.Button(self, text="Calc", command=self.calculate).pack(side="bottom")
        self.entry1.pack(side="left")
        self.operator.pack(side="left")
        self.entry2.pack(side="left")
        self.result.pack(side="left")

    def calculate(self):
        try:
            val = int(self.entry1.get()) + int(self.entry2.get())
            self.result.config(text=str(val))
        except:
            self.result.config(text="Error")
