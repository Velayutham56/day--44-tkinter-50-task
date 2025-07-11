import tkinter as tk

def left(event): canvas.move(rect, -10, 0)
def right(event): canvas.move(rect, 10, 0)

root = tk.Tk()
root.title("Move Rectangle")
canvas = tk.Canvas(root, width=300, height=200, bg="lightblue")
canvas.pack()

rect = canvas.create_rectangle(50, 50, 100, 100, fill="red")
root.bind("<Left>", left)
root.bind("<Right>", right)

root.mainloop()
