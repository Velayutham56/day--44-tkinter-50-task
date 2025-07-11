import tkinter as tk

root = tk.Tk()

def toggle_all():
    current = entry["state"]
    new_state = "normal" if current == "disabled" else "disabled"
    entry.config(state=new_state)
    button.config(state=new_state)
    label.config(fg="black" if new_state == "normal" else "gray")

entry = tk.Entry(root, state="normal")
entry.pack()

button = tk.Button(root, text="Entry + Label Toggle", state="normal")
button.pack()

label = tk.Label(root, text="Status Label", fg="black")
label.pack()

toggle_btn = tk.Button(root, text="Toggle All", command=toggle_all)
toggle_btn.pack()

root.mainloop()
