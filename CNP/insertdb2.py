import sqlite3

class MainInsert:
    def __init__(self, name, surname, cnp):
        self.name = name
        self.surname = surname
        self.cnp = cnp

    def database(self):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('CNP/db2.db')
            cursor = conn.cursor()

            # Create a table
            create_table_command = '''
            CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL,
                surname TEXT UNIQUE NOT NULL,
                cnp TEXT PRIMARY KEY
            )
            '''
            cursor.execute(create_table_command)
            conn.commit()

            # Insert data
            insert_data_command = '''
            INSERT INTO users (name, surname, cnp)
            VALUES (?, ?, ?)
            '''
            data = (self.name, self.surname, self.cnp)
            cursor.execute(insert_data_command, data)
            conn.commit()

        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}")  # Handle unique constraint violation
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")  # Handle other SQLite errors
        finally:
            # Close the connection
            cursor.close()
            conn.close()