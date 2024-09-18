import sqlite3
import re

class InvalidInsert(Exception):
    def __init__(self, message="Invalid CNP provided", code=None):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"{self.__class__.__name__}: {self.message}"

class MainInsert:
    def __init__(self, name, surname, cnp, msg):
        self.name = name
        self.surname = surname
        self.cnp = cnp
        self.msg = msg
        self.database_path = 'CNP/db2.db'
        self._validate_cnp()

    def _validate_cnp(self):
        if not re.match(r'^\d{13}$', self.cnp):
            raise InvalidInsert("CNP must be a 13-digit number.")

    def _connect(self):
        return sqlite3.connect(self.database_path)

    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            create_table_command = '''
            CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                cnp TEXT PRIMARY KEY,
                msg TEXT NOT NULL
            )
            '''
            cursor.execute(create_table_command)

    def insert_data(self):
        self._create_table()

        try:
            with self._connect() as conn:
                cursor = conn.cursor()
                insert_data_command = '''
                INSERT INTO users (name, surname, cnp, msg)
                VALUES (?, ?, ?, ?)
                '''
                data = (self.name, self.surname, self.cnp, self.msg)
                cursor.execute(insert_data_command, data)
                conn.commit()
        except sqlite3.IntegrityError as e:
            raise InvalidInsert(f"IntegrityError: {e}")
        except sqlite3.Error as e:
            raise Exception(f"SQLite Error: {e}")