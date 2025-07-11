import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

def draw_circle(event):
    r = 5
    x, y = event.x, event.y
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="blue")

canvas.bind("<Button-1>", draw_circle)

root.mainloop()
