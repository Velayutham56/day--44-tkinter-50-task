import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

start = None

def click(event):
    global start
    if not start:
        start = (event.x, event.y)
    else:
        canvas.create_rectangle(start[0], start[1], event.x, event.y, outline="green")
        start = None

canvas.bind("<Button-1>", click)

root.mainloop()
