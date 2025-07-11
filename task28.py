import tkinter as tk

def submit(event=None):
    print("Username entered:", entry.get())

root = tk.Tk()
root.title("Login Form")

entry = tk.Entry(root)
entry.pack(pady=10)
entry.bind("<Return>", submit)

tk.Button(root, text="Submit", command=submit).pack()
root.mainloop()
