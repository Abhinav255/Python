from db_connection import DBConnection
import hashlib

class ProductManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def register(self, name, email, password, role):
        try:
            # Hash the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Insert product manager data into database
            query = "INSERT INTO product_managers (name, email, password, role) VALUES (%s, %s, %s, %s)"
            self.db_connection.execute_query(query, (name, email, hashed_password, role))
            return True
        except Exception as e:
            print("Error:", e)
            return False

    def login(self, email, password):
        try:
            # Hash the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Check if email and hashed password match in the database
            query = "SELECT * FROM product_managers WHERE email = %s AND password = %s"
            result = self.db_connection.execute_query(query, (email, hashed_password))

            if result.fetchone():
                return True
            else:
                return False
        except Exception as e:
            print("Error:", e)
            return False

    def manage_stocks(self, product_id, action):
        try:
            # Implement logic to manage product stocks
            pass
        except Exception as e:
            print("Error:", e)

    def view_stocks(self):
        try:
            # Implement logic to view all product stocks
            pass
        except Exception as e:
            print("Error:", e)
