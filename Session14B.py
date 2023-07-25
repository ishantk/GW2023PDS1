import mysql.connector as db


class DBHelper:

    def __init__(self):
        # Step1: Create Connection with Database
        self.connection = db.connect(user='root',
                                password='',
                                # port='3306',
                                host='127.0.0.1',
                                database='gw2023pds1')

        # Step2: Obtain Cursor to perform SQL operations :)
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection Created and Cursor Obtained...")

    # Insert, Update and Delete i.e. Write into Database
    def execute_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] SQL Statement Executed...")

    # Select Operation i.e. Read from Database
    def execute_select_sql(self, sql):
        print("[DBHelper] Executing SQL:", sql)
        # Step3: Execute SQL Command
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

