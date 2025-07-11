import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root, highlightthickness=2, highlightbackground="gray")
entry.pack()

entry.bind("<Enter>", lambda e: entry.config(highlightbackground="red"))
entry.bind("<Leave>", lambda e: entry.config(highlightbackground="gray"))

root.mainloop()
