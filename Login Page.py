import tkinter as tk
from tkinter import messagebox
import random

class WelcomePage:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Welcome Page")

        # Welcome message
        tk.Label(root, text="Welcome, {}!".format(username)).pack()

        # Logout button
        tk.Button(root, text="Logout", command=self.logout).pack()

    def logout(self):
        # Destroy the current welcome window and show the login page
        self.root.destroy()
        login_page.show_login_page()

class RegistrationPage:
    def __init__(self, root, login_page, user_database):
        self.root = root
        self.login_page = login_page
        self.user_database = user_database
        self.root.title("Registration Page")

        # Variables to store the registration information
        self.name_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.gmail_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.agree_var = tk.BooleanVar()

        # Entry widgets for registration details
        tk.Label(root, text="Name").pack()
        tk.Entry(root, textvariable=self.name_var).pack()

        tk.Label(root, text="Username (Gmail)").pack()
        tk.Entry(root, textvariable=self.username_var).pack()

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, show="*")
        self.password_entry.pack()

        tk.Label(root, text="Gmail").pack()
        tk.Entry(root, textvariable=self.gmail_var).pack()

        tk.Label(root, text="Age").pack()
        tk.Entry(root, textvariable=self.age_var).pack()

        tk.Label(root, text="Address").pack()
        tk.Entry(root, textvariable=self.address_var).pack()

        tk.Label(root, text="Phone").pack()
        tk.Entry(root, textvariable=self.phone_var).pack()

        tk.Checkbutton(root, text="I agree to the terms", variable=self.agree_var).pack()

        # Show Password checkbox
        tk.Checkbutton(root, text="Show Password", command=self.toggle_password_visibility).pack()

        # Register button
        tk.Button(root, text="Register", command=self.register).pack()

        # Back button
        tk.Button(root, text="Back to Login", command=self.back_to_login).pack()

    def toggle_password_visibility(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def register(self):
        new_name = self.name_var.get()
        new_username = self.username_var.get()
        new_password = self.password_var.get()
        new_gmail = self.gmail_var.get()
        new_age = self.age_var.get()
        new_address = self.address_var.get()
        new_phone = self.phone_var.get()
        agree_to_terms = self.agree_var.get()

        if new_name and new_username and new_password and new_gmail and new_age and new_address and new_phone and agree_to_terms:
            if "@" in new_username and new_username.endswith("@gmail.com"):
                if new_username not in self.user_database:
                    self.user_database[new_username] = new_password
                    messagebox.showinfo("Registration Successful", "Account created for {}".format(new_username))
                    # For now, we'll simply go back to the login page
                    self.login_page.show_login_page()
                else:
                    messagebox.showerror("Registration Failed", "Username already exists")
            else:
                messagebox.showerror("Registration Failed", "Please enter a valid Gmail address")
        else:
            messagebox.showerror("Registration Failed", "Please enter all registration details and agree to the terms")

    def back_to_login(self):
        # Destroy the current registration window and show the login page
        self.root.destroy()
        self.login_page.show_login_page()

class ForgotPasswordPage:
    def __init__(self, root, login_page, user_database):
        self.root = root
        self.login_page = login_page
        self.user_database = user_database
        self.root.title("Forgot Password")

        # Variables to store the entered information
        self.username_var = tk.StringVar()

        # Entry widget for username (email address)
        tk.Label(root, text="Enter Username (Gmail)").pack()
        tk.Entry(root, textvariable=self.username_var).pack()

        # Submit button
        tk.Button(root, text="Submit", command=self.send_reset_email).pack()

        # Back button
        tk.Button(root, text="Back to Login", command=self.back_to_login).pack()

    def send_reset_email(self):
        username = self.username_var.get()

        if username in self.user_database:
            # Generate a temporary password
            temp_password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))

            # Update the user's password in the database
            self.user_database[username] = temp_password

            messagebox.showinfo("Password Reset", "A temporary password has been sent to your email.")
            self.root.destroy()
            self.login_page.show_login_page()
        else:
            messagebox.showerror("Invalid Username", "Username not found. Please enter a valid username.")

    def back_to_login(self):
        # Destroy the current forgot password window and show the login page
        self.root.destroy()
        self.login_page.show_login_page()

class LoginPage:
    def __init__(self, root, user_database):
        self.root = root
        self.root.title("Login Page")
        self.user_database = user_database

        # Variables to store the username and password
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Entry widgets for username and password
        tk.Label(root, text="Username (Gmail)").pack()
        tk.Entry(root, textvariable=self.username_var).pack()

        tk.Label(root, text="Password").pack()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, show="*")
        self.password_entry.pack()

        # Show Password checkbox
        tk.Checkbutton(root, text="Show Password", command=self.toggle_password_visibility).pack()

        # Login button
        tk.Button(root, text="Login", command=self.login).pack()

        # Registration button
        tk.Button(root, text="Register", command=self.show_registration_page).pack()

        # Forgot Password button
        tk.Button(root, text="Forgot Password", command=self.show_forgot_password_page).pack()

        # Set the dimensions of the window
        self.root.geometry("400x300")  # Adjust width and height as needed

    def toggle_password_visibility(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def login(self):
        entered_username = self.username_var.get()
        entered_password = self.password_var.get()

        if entered_username in self.user_database and self.user_database[entered_username] == entered_password:
            # Hide the login page and show the welcome page
            self.root.withdraw()
            welcome_page = tk.Toplevel(self.root)
            WelcomePage(welcome_page, entered_username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_registration_page(self):
        # Hide the login page and show the registration page
        self.root.withdraw()  # Hide the login page
        registration_page = tk.Toplevel(self.root)  # Create a new top-level window for registration
        RegistrationPage(registration_page, self, self.user_database)  # Initialize the RegistrationPage

    def show_forgot_password_page(self):
        # Hide the login page and show the forgot password page
        self.root.withdraw()  # Hide the login page
        forgot_password_page = tk.Toplevel(self.root)  # Create a new top-level window for forgot password
        ForgotPasswordPage(forgot_password_page, self, self.user_database)  # Initialize the ForgotPasswordPage

    def show_login_page(self):
        # Show the login page
        self.root.deiconify()

if __name__ == "__main__":
    user_database = {}  # Database to store registered users and passwords
    root = tk.Tk()
    login_page = LoginPage(root, user_database)
    root.mainloop()
