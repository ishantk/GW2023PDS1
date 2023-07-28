import datetime


class Customer:

    def __init__(self):
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
        self.createdon = datetime.datetime.today()

