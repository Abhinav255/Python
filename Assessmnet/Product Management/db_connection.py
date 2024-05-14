import mysql.connector

class DBConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="product_management"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        # Execute SQL query
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def close_connection(self):
        # Close database connection
        self.cursor.close()
        self.connection.close()
