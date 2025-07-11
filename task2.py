import tkinter as tk

root = tk.Tk()

def toggle_entry():
    entry.config(state="disabled" if chk_var.get() else "normal")

chk_var = tk.IntVar()
check = tk.Checkbutton(root, text="Disable Entry", variable=chk_var, command=toggle_entry)
check.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()
