import tkinter as tk

def enlarge(event):
    label.config(font=('Arial', 20, 'bold'))

def shrink(event):
    label.config(font=('Arial', 12))

root = tk.Tk()
label = tk.Label(root, text="Hover Over Me", font=('Arial', 12))
label.pack(pady=20)
label.bind("<Enter>", enlarge)
label.bind("<Leave>", shrink)
root.mainloop()
