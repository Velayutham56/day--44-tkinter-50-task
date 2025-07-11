import tkinter as tk

root = tk.Tk()

def lock_entry():
    entry.config(state="disabled")

entry = tk.Entry(root)
entry.pack()

lock_btn = tk.Button(root, text="Lock Entry", command=lock_entry)
lock_btn.pack()

root.mainloop()
