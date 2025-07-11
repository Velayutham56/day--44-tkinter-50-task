import tkinter as tk

root = tk.Tk()

buttons = []

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

for i in range(5):
    btn = tk.Button(root, text=f"Button {i+1}")
    btn.pack()
    buttons.append(btn)

disable_btn = tk.Button(root, text="Disable All", command=disable_all)
disable_btn.pack()

root.mainloop()
