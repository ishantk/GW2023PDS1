from Session14A import Customer
from Session14B import DBHelper


def main():

    db = DBHelper()

    print("Welcome to VetsApp")

    message = """
    1: Add New Customer
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice:"))

    while True:
        if choice == 1:
            customer = Customer()
            customer.read_customer_data()
            print(vars(customer))

            # Adding Customer to Database
            sql = customer.get_insert_sql_query()
            db.execute_sql(sql)

        elif choice == 0:
            print("Thank You for Using VetsApp")
            break
        else:
            print("Invalid Choice..")

        print(message)
        choice = int(input("Enter Your Choice:"))


if __name__ == "__main__":
    main()
