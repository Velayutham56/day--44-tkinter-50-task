import tkinter as tk

root = tk.Tk()

log = tk.Text(root, width=40, height=10)
log.pack()

def log_event(event):
    msg = f"{event.type} at ({event.x},{event.y})\n"
    log.insert("end", msg)

root.bind("<Button-1>", log_event)
root.bind("<Enter>", log_event)
root.bind("<Leave>", log_event)

root.mainloop()
