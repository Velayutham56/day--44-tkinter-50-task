import tkinter as tk

def on_release(event):
    if event.keysym in ["Shift_L", "Shift_R"]:
        print("Shift key released!")

root = tk.Tk()
root.title("Shift Tracker")
root.bind("<KeyRelease>", on_release)
root.mainloop()
