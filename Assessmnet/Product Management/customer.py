from db_connection import DBConnection

import tkinter as tk
from tkinter import messagebox
from db_connection import DBConnection
from customer import Customer

class Customer:
    def __init__(self, db_connection):
        self.db_connection = db_connection

class CustomerRegistrationForm(tk.Toplevel):
    def __init__(self, db_connection):
        super().__init__()
        self.title("Customer Registration")
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

        tk.Label(self, text="Address:").pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        tk.Button(self, text="Register", command=self.register_customer).pack()

    def register_customer(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        address = self.address_entry.get()

        # Validate inputs
        if not name or not email or not password or not address:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Create customer object and register
        customer = Customer(self.db_connection)
        success = customer.register(name, email, password, address)

        if success:
            messagebox.showinfo("Success", "Registration successful!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Registration failed. Please try again.")

if __name__ == "__main__":
    # Create a database connection
    db_connection = DBConnection()

    # Create and run the customer registration form
    root = tk.Tk()
    customer_registration_form = CustomerRegistrationForm(db_connection)
    root.mainloop()




    # Implement customer methods
