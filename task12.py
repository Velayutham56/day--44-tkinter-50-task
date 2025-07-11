import tkinter as tk

root = tk.Tk()

def toggle_color():
    if button["state"] == "normal":
        button.config(state="disabled", bg="gray", fg="white")
    else:
        button.config(state="normal", bg="lightblue", fg="black")

button = tk.Button(root, text="Toggle Me", bg="lightblue", fg="black", command=toggle_color)
button.pack()

root.mainloop()
