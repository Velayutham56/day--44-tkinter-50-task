import tkinter as tk

class LoginWidget(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack()
        
        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack()

        tk.Button(self, text="Login", command=self.login).pack()

    def login(self):
        print(f"User: {self.username.get()}, Pass: {self.password.get()}")
