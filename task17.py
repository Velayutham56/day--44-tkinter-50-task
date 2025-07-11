import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hover Me", bg="white", fg="black")
label.pack()

label.bind("<Enter>", lambda e: label.config(fg="red"))
label.bind("<Leave>", lambda e: label.config(fg="black"))

root.mainloop()
