"""
    Shopping Cart
"""


def apply_promo_code(amount, promo_code):
    if promo_code == "WELCOME50":
        if amount >= 159:
            print("Promo Code Applied Successfully...")

            discount = 0.50 * amount

            if discount >= 100:
                discount = 100

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)

    elif promo_code == "ZOMPAYTM":
        if amount >= 299:
            print("Promo Code Applied Successfully...")

            discount = 0.20 * amount

            if discount >= 50:
                discount = 50

            amount_to_pay = amount - discount
            print("Please Pay: \u20b9", amount_to_pay)
            print("You will get a cashback of: \u20b9 25")
        else:
            print("Amount is Lesser for Promo Code...")
            print("Please Pay: \u20b9", amount)
    else:
        print("Promo Code Invalid")
        print("Please Pay: \u20b9", amount)


def main():

    menu = {
        "dal": 300,
        "parantha": 40,
        "noodles": 250,
        "burger": 150,
        "fries": 100,
        "cola": 50,
    }

    print("MENU:")
    print(menu)

    item_names = []
    quantities = []
    food_cart = []  # price

    while True:
        item_name = input("Enter Dish Name to add in Cart: ")
        quantity = int(input("Enter Dish Quantity: "))
        item_names.append(item_name)
        quantities.append(quantity)
        price = menu[item_name] * quantity
        food_cart.append(price)

        choice = input("Do You wish to add more items? (yes/no)")
        if choice == "no":
            break

    print(item_names)
    print(quantities)
    print(food_cart)

    amount = sum(food_cart)
    print("TOTAL AMOUNT: \u20b9", amount)

    message = """
        Welcome to Zomato
        OFFERS FOR TODAY

        WELCOME50
        Get 50% OFF up to ₹100
        Valid on total value of items worth ₹159 or more.


        ZOMPAYTM
        Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
        Valid on total value of items worth ₹299 or more.


    """

    print(message)
    promo_code = input("Enter Promo Code: ")
    apply_promo_code(amount, promo_code)


if __name__ == "__main__":
    main()


# Assignment: Implement the same program Using OOPS from Session7 and Session7A

