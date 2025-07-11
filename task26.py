import tkinter as tk

def log_key(event):
    print("Pressed key:", event.keysym)

root = tk.Tk()
root.title("Key Logger")
root.bind("<KeyPress>", log_key)
root.mainloop()
