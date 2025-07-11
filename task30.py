import tkinter as tk

def toggle_color(event):
    if event.char.lower() == 'b':
        root.config(bg="black")
    elif event.char.lower() == 'w':
        root.config(bg="white")

root = tk.Tk()
root.title("Background Toggle")
root.geometry("300x150")
root.bind("<Key>", toggle_color)
root.mainloop()
