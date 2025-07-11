import tkinter as tk

root = tk.Tk()

def enable_submit():
    submit_btn.config(state="normal" if agree_var.get() else "disabled")

agree_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="I agree", variable=agree_var, command=enable_submit)
checkbox.pack()

submit_btn = tk.Button(root, text="Submit", state="disabled")
submit_btn.pack()

root.mainloop()
