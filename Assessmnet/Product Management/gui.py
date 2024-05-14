import tkinter as tk
from product_manager import ProductManager
from customer import Customer
from db_connection import DBConnection

class ProductManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Product Management Application")
        self.geometry("600x400")

        # Initialize database connection
        self.db_connection = DBConnection()

        # Initialize product manager and customer objects
        self.product_manager = ProductManager(self.db_connection)
        self.customer = Customer(self.db_connection)

        # Initialize GUI components
        self.create_widgets()

    def create_widgets(self):
        # Create buttons for product manager and customer
        product_manager_btn = tk.Button(self, text="Product Manager", command=self.product_manager_menu)
        product_manager_btn.pack(pady=10)
        
        customer_btn = tk.Button(self, text="Customer", command=self.customer_menu)
        customer_btn.pack(pady=10)

    def product_manager_menu(self):
        # Implement product manager menu
        pass

    def customer_menu(self):
        # Implement customer menu
        pass

if __name__ == "__main__":
    app = ProductManagementApp()
    app.mainloop()
