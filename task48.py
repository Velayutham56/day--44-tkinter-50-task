import tkinter as tk

def toggle_visibility():
    entry.config(show='' if entry.cget('show') == '*' else '*')

root = tk.Tk()
entry = tk.Entry(root, show='*', width=20)
entry.pack(pady=5)

button = tk.Button(root, text="Show/Hide", command=toggle_visibility)
button.pack(pady=5)
root.mainloop()
