import tkinter as tk

class RatingBar(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.stars = []
        self.rating = 0
        for i in range(5):
            btn = tk.Button(self, text="☆", font=("Arial", 20), command=lambda i=i: self.set_rating(i + 1))
            btn.pack(side="left")
            self.stars.append(btn)

    def set_rating(self, r):
        self.rating = r
        for i, btn in enumerate(self.stars):
            btn.config(text="★" if i < r else "☆")
