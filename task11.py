import tkinter as tk

root = tk.Tk()

entries = []
buttons = []

def reset_all():
    for e in entries:
        e.config(state="normal")
    for b in buttons:
        b.config(state="normal")

entry1 = tk.Entry(root, state="disabled")
entry1.pack()
entries.append(entry1)

button1 = tk.Button(root, text="Disabled Button", state="disabled")
button1.pack()
buttons.append(button1)

reset_btn = tk.Button(root, text="Reset All", command=reset_all)
reset_btn.pack()

root.mainloop()
