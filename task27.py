import tkinter as tk

def display_key(event):
    label.config(text=f"Pressed: {event.keysym}")

root = tk.Tk()
root.title("Show Key")
label = tk.Label(root, text="Press a key...", font=("Helvetica", 16))
label.pack(pady=20)

root.bind("<KeyPress>", display_key)
root.mainloop()
