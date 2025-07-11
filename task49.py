import tkinter as tk

def update_progress():
    current = label.cget("text")
    if len(current) < 10:
        label.config(text=current + "#")

root = tk.Tk()
label = tk.Label(root, text="", font=('Courier', 16))
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=update_progress)
button.pack(pady=10)
root.mainloop()
