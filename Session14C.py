from Session14A import Customer
from Session14B import DBHelper
import pandas as pd               # pip install pandas
from tabulate import tabulate     # pip install tabulate


def main():

    db = DBHelper()

    print("Welcome to VetsApp")

    message = """
    0: Quit
    1: Add New Customer
    2: Update Existing Customer
    3: Delete Customer
    4: View All Customers
    5: View Customer by Phone
    """
    print(message)
    choice = int(input("Enter Your Choice:"))

    # Create a single customer object
    customer = Customer()

    while True:
        if choice == 1:
            customer.read_customer_data()
            print(vars(customer))

            # Adding Customer to Database
            sql = customer.get_insert_sql_query()
            db.execute_sql(sql)

        elif choice == 2:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            customer.name = input("Enter Customer Name: ")
            if len(customer.name) == 0:
                customer.name = customer_fetched[1]

            customer.phone = input("Enter Customer Phone: ")
            if len(customer.phone) == 0:
                customer.phone = customer_fetched[2]

            customer.email = input("Enter Customer Email: ")
            if len(customer.email) == 0:
                customer.email = customer_fetched[3]

            customer.age = input("Enter Customer Age: ")
            if len(customer.age) == 0:
                customer.age = customer_fetched[4]
            else:
                customer.age = int(customer.age)

            customer.gender = input("Enter Customer Gender: ")
            if len(customer.gender) == 0:
                customer.gender = customer_fetched[5]

            customer.address = input("Enter Customer Address: ")
            if len(customer.address) == 0:
                customer.address = customer_fetched[6]

            sql = customer.get_update_sql_query()
            db.execute_sql(sql)
            print("Customer Updated...")

        elif choice == 3:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            delete_choice = input("Are Your Sure to Delete ? (yes/no): ")

            if delete_choice == "yes":
                sql = customer.get_delete_sql_query()
                db.execute_sql(sql)
                print("Customer Deleted...")

        elif choice == 4:
            sql = customer.get_customers_sql_query()
            rows = db.execute_select_sql(sql)
            # for row in rows:
            #     print(row)

            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            # table = pd.DataFrame(rows, columns=columns)
            # pd.set_option('display.max_rows', None)
            # pd.set_option('display.max_columns', None)
            # print(table)

        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            # for row in rows:
            #     print(row)

            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            print("Thank You for Using VetsApp")
            break
        else:
            print("Invalid Choice..")

        print(message)
        choice = int(input("Enter Your Choice:"))


if __name__ == "__main__":
    main()
