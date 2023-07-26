def consultation_menu():
    message = """
       >>Consultation Menu<<
       1: Add Consultation
       2: Update Consultation
       3: View All Consultations
       4: View Consultations by Date
       5: View Customers Pets Consultation
       0: Quit
       """
    print(message)
    choice = int(input("Enter Your Choice: "))

    while True:
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice: "))