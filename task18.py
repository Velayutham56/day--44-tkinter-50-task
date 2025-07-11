import tkinter as tk
import random

root = tk.Tk()
root.geometry("300x300")

def move_button():
    x = random.randint(0, 250)
    y = random.randint(0, 250)
    btn.place(x=x, y=y)

btn = tk.Button(root, text="Catch Me!", command=move_button)
btn.place(x=100, y=100)

root.mainloop()
