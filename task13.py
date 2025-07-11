import tkinter as tk

root = tk.Tk()

def toggle_spin():
    spin.config(state="disabled" if chk_var.get() else "normal")

chk_var = tk.IntVar()
check = tk.Checkbutton(root, text="Disable Spinbox", variable=chk_var, command=toggle_spin)
check.pack()

spin = tk.Spinbox(root, from_=0, to=10)
spin.pack()

root.mainloop()
