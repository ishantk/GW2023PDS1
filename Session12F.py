"""
    DataBase : MySQL
    Collection of Tables, used to store data permanently
    Data should be structured

    Persistence: To Save data of an object permanently

    ORM: Object Relational Mapping

    SQL
    create table Customer(
        cid int primary key auto_increment
        name text,
        phone text,
        email text,
        age int,
        gender text
    )

    # SQL
    insert into Customer values(null, 'John', '99112 22112', 'john@example.com', 21, 'male')

    # Python
    # customer = Customer('John', '99112 22112', 'john@example.com', 21, 'male')

"""


class Customer:

    def __init__(self):
        self.name = input("Enter Name: ")
        self.phone = input("Enter Phone: ")
        self.email = input("Enter Email: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def show(self):
        print("Name: {name} Phone:{phone} Email:{email}".format_map(vars(self)))


def main():
    message = """Welcome to CRM App
    1: Add New Customer
    2: Delete Customer
    3: Update Customer
    4: View All Customers
    5: View Customer by Phone
    6: Exit
    """

    print(message)
    choice = int(input("Enter Your Choice: "))

    while(True):
        if choice == 1:
            customer = Customer()
            customer.show()

        choice = int(input("Enter Your Choice: "))
        if choice == 6:
            break


if __name__ == "__main__":
    main()