

import tkinter as tk
from tkinter import messagebox
from db_connection import DBConnection
from product_manager import ProductManager

class ProductManagerRegistrationForm(tk.Toplevel):
    def __init__(self, db_connection):
        super().__init__()
        self.title("Product Manager Registration")
        self.geometry("400x300")
        self.db_connection = db_connection

        # Create labels and entry fields
        tk.Label(self, text="Name:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Password:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Label(self, text="Role:").pack()
        self.role_entry = tk.Entry(self)
        self.role_entry.pack()

        tk.Button(self, text="Register", command=self.register_product_manager).pack()

    def register_product_manager(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.role_entry.get()

        # Validate inputs
        if not name or not email or not password or not role:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create product manager object and register
        product_manager = ProductManager(self.db_connection)
        success = product_manager.register(name, email, password, role)

        if success:
            messagebox.showinfo("Success", "Registration successful!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Registration failed. Please try again.")

if __name__ == "__main__":
    # Create a database connection
    db_connection = DBConnection()

    # Create and run the product manager registration form
    root = tk.Tk()
    product_manager_registration_form = ProductManagerRegistrationForm(db_connection)
    root.mainloop()

class ProductManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Manager Dashboard")
        self.geometry("600x400")
        self.db_connection = DBConnection()

        # Initialize product manager object
        self.product_manager = None

        # Initialize GUI components
        self.create_widgets()

    def create_widgets(self):
        # Create buttons for various functionalities
        register_btn = tk.Button(self, text="Register", command=self.register_product_manager)
        register_btn.pack(pady=10)

        login_btn = tk.Button(self, text="Login", command=self.login_product_manager)
        login_btn.pack(pady=10)

        manage_stocks_btn = tk.Button(self, text="Manage Stocks", command=self.manage_stocks)
        manage_stocks_btn.pack(pady=10)

        view_stocks_btn = tk.Button(self, text="View Stocks", command=self.view_stocks)
        view_stocks_btn.pack(pady=10)

    def register_product_manager(self):
        # Implement product manager registration form
        pass

    def login_product_manager(self):
        # Implement product manager login form
        pass

    def manage_stocks(self):
        # Implement functionality to manage product stocks
        pass

    def view_stocks(self):
        # Implement functionality to view all product stocks
        pass
