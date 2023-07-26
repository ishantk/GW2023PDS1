from Session16A import customer_menu
from Session16B import pets_menu
from Session16C import consultation_menu
import datetime


def main_menu():
    message = """
    >>Main Menu<<
    1: Manage Customers
    2: Manage Pets
    3: Manage Consultations
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice: "))

    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            consultation_menu()
        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice: "))


def main():

    date1 = datetime.datetime.today() # to use this -> import datetime

    welcome = """
    ~~~~~~~~~~~~~~~~~~~
    Welcome to Vets App
    ~~~~~~~~~~~~~~~~~~~
    """
    print(welcome)

    main_menu()

    bye_message = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Thank You for Using Vets App
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    print(bye_message)

    date2 = datetime.datetime.today()
    print("App Usage:", date2-date1)


if __name__ == "__main__":
    main()

