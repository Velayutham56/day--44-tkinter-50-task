import tkinter as tk

root = tk.Tk()

def update_controls():
    state = radio_var.get()
    entry.config(state="normal" if state == "Unlock" else "disabled")
    button.config(state="normal" if state == "Unlock" else "disabled")

radio_var = tk.StringVar(value="Lock")

tk.Radiobutton(root, text="Lock", variable=radio_var, value="Lock", command=update_controls).pack()
tk.Radiobutton(root, text="Unlock", variable=radio_var, value="Unlock", command=update_controls).pack()

entry = tk.Entry(root, state="disabled")
entry.pack()

button = tk.Button(root, text="I Get Locked", state="disabled")
button.pack()

root.mainloop()
