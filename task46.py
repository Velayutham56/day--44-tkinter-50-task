import tkinter as tk

def change_color(event):
    label.config(bg='lightblue' if label.cget('bg') == 'yellow' else 'yellow')

root = tk.Tk()
label = tk.Label(root, text="Click Me!", bg='yellow', font=('Arial', 16), width=20)
label.pack(pady=20)
label.bind("<Button-1>", change_color)
root.mainloop()
