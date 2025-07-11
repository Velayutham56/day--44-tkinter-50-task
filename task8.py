import tkinter as tk

root = tk.Tk()

button = tk.Button(
    root,
    text="Hover to Activate",
    state="normal",
    activebackground="lightgreen",
    activeforeground="blue"
)
button.pack()

root.mainloop()
