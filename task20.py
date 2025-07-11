import tkinter as tk

root = tk.Tk()

def show_tooltip(event):
    tip.place(x=event.x_root - root.winfo_rootx(), y=event.y_root - root.winfo_rooty())

def hide_tooltip(event):
    tip.place_forget()

label = tk.Label(root, text="Hover for Info")
label.pack()

tip = tk.Label(root, text="Tooltip Text", bg="yellow", relief="solid", bd=1)
label.bind("<Enter>", show_tooltip)
label.bind("<Leave>", hide_tooltip)

root.mainloop()
