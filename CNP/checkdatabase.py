import sqlite3

def check_cnp_exists(cnp):
    try:
        # Connect to SQLite database
        conn = sqlite3.connect('CNP/db2.db')
        cursor = conn.cursor()

        # SQL query to check if the CNP exists
        query = 'SELECT COUNT(*) FROM users WHERE cnp = ?'
        cursor.execute(query, (cnp,))

        return True  # Return True if the CNP exists, False otherwise

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
        return False  # Return False in case of an error

    finally:
        # Close the connection
        cursor.close()
        conn.close()