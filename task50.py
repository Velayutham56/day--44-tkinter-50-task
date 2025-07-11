import tkinter as tk

def count_characters(event):
    count_label.config(text=f"Characters: {len(entry.get())}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=5)
entry.bind("<KeyRelease>", count_characters)

count_label = tk.Label(root, text="Characters: 0")
count_label.pack(pady=5)
root.mainloop()
