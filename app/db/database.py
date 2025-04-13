import sqlite3
import os

class Database:
    def __init__(self, database_file):
        self.database_file = database_file
        self._initDB()

    def _initDB(self):
        if not os.path.isfile(self.database_file):
            try:
                with sqlite3.connect(self.database_file, check_same_thread=False) as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS POSTS (
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            description TEXT NOT NULL,
                            date TEXT NOT NULL
                            )
                    """)

                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS USERS (
                        email TEXT PRIMARY KEY,
                        password TEXT NOT NULL
                        )
                    """)

                    print("Database configured successfully!")
                    
                    conn.commit()
            except sqlite3.OperationalError as err:
                print("Failed to setup database:", err)
        else:
            print("Database already exists, no need to initialize.")

    def get_connection(self):
        return sqlite3.connect(self.database_file, check_same_thread=False)
