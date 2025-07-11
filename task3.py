import tkinter as tk

root = tk.Tk()

def disable_other():
    button2.config(state="disabled")

button1 = tk.Button(root, text="Disable Second", command=disable_other)
button1.pack()

button2 = tk.Button(root, text="I get disabled")
button2.pack()

root.mainloop()
