import sqlite3


class Database:
    """
    Class for working with SQLite database.
    """

    def __init__(self, db_name):
        """
        Initialize an object of the Database class.

        Parameters:
            db_name (str): Name of the database.
         """
        self.db_name = db_name
        self.connection = None

    def connect(self):
        """
        Establish a connection to the database.
        """
        self.connection = sqlite3.connect(self.db_name)

    def create_table(self):
        """
        Create the necessary tables if they don't exist.

        This method creates two tables: 'consumers' and 'orders'.
        """
        if not self.connection:
            raise ValueError("No connection to DB")
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consumers(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            city TEXT
            )
        """)
        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS orders(
                    id INTEGER PRIMARY KEY,
                    human_id INTEGER,
                    item TEXT,
                    quantity INTEGER,
                    FOREIGN KEY (human_id) REFERENCES consumers (id)
                    )
                """)
        self.connection.commit()

    def execute(self, query):
        """
        Execute an SQL query to modify data in the database.

        Parameters:
             query (str): SQL query to execute.
        """
        if not self.connection:
            raise ValueError("No connection to DB")
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def select(self, query):
        """
        Execute an SQL query to retrieve data from the database.

        Parameters:
            query (str): SQL query to execute.

        Returns:
            list: List of rows obtained as a result of the query.
        """
        if not self.connection:
            raise ValueError("No connection to DB")
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def close(self):
        """
        Close the connection to the database.
        """
        if self.connection:
            self.connection.close()
