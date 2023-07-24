import mysql.connector as db


class DBHelper:

    def __init__(self):
        # Step1: Create Connection with Database
        self.connection = db.connect(user='root',
                                password='',
                                host='127.0.0.1',
                                database='gw2023pds1')

        # Step2: Obtain Cursor to perform SQL operations :)
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection Created and Cursor Obtained...")

    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL Statement Executed...")