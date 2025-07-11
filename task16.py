import tkinter as tk

root = tk.Tk()

def show_coords(event):
    print(f"Mouse clicked at: ({event.x}, {event.y})")

btn = tk.Button(root, text="Click Me")
btn.bind("<Button-1>", show_coords)
btn.pack()

root.mainloop()
