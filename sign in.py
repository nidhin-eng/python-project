import tkinter as tk
from tkinter import messagebox

class SignUpWindow:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up")

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.sign_up_button = tk.Button(self.master, text="Sign Up",bg='white',fg='violet', command=self.sign_up)
        self.sign_up_button.pack()

    def sign_up(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        with open("user_credentials.txt", "a") as file:
            file.write(f"{username}:{password}\n")

        messagebox.showinfo("Success", "Sign up successful!")
        self.master.destroy()
        self.show_login_window()

    def show_login_window(self):
        login_root = tk.Tk()
        login_app = LoginWindow(login_root)
        login_root.configure(bg='black')
        login_root.mainloop()

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login",bg='white',fg='violet', command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        with open("user_credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Success", f"Welcome, {username}!")
                    self.master.destroy()
                    return

        messagebox.showerror("Error", "Invalid username or password.")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg='black')
    sign_up_app = SignUpWindow(root)
    root.mainloop()
