import datetime

"""
    create table Customer(
        cid int primary key auto_increment,
        name text,
        phone text unique key,
        email text,
        age int,
        gender text,
        address text,
        createdon datetime
    );
"""


class Customer:

    def __init__(self):
        self.cid = 0
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customer Email: ")
        self.age = int(input("Enter Customer Age: "))
        self.gender = input("Enter Customer Gender (male/female): ").lower()
        self.address = input("Enter Customer Address: ")
        # Get the date and time
        self.createdon = str(datetime.datetime.today())
        # Eliminate Milli Seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', {age}, " \
              "'{gender}', '{address}', '{createdon}');".format_map(vars(self))
        return sql

    def get_customers_sql_query(self, phone=""):

        if len(phone) == 0:
            sql = "select * from Customer"
        else:
            sql = "select * from Customer where phone = '{}'".format(phone)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from Customer where cid = {}".format(self.cid)
        return sql

    def get_update_sql_query(self):
        sql = "update Customer set name='{name}', phone='{phone}', email='{email}', age={age}, " \
              "gender='{gender}', address='{address}' where cid = {cid}".format_map(vars(self))
        return sql


