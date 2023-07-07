message = """
    Welcome to Zomato
      SUBWAY OFFERS
      
    WELCOME50
    Get 50% OFF up to ₹100
    Valid on total value of items worth ₹159 or more.

    
    ZOMPAYTM
    Get 20% OFF up to ₹50 and ₹25 Paytm cashback using Paytm
    Valid on total value of items worth ₹299 or more.

    
"""

# PEP
# https://peps.python.org/pep-0008/

print(message)
amount = int(input("Enter Total Amount: "))
promo_code = input("Enter Promo Code: ")

# Simple or Regular if/else
"""
if amount >= 159:
    print("You can Apply Promo Code...")
else:
    print("You cannot Apply Promo Code...")
"""

# Nested if/else
"""
if amount >= 159:
    if promo_code == "WELCOME50":
        print("Promo Code Applied Successfully...")

        discount = 0.50 * amount

        if discount >= 100:
            discount = 100

        amount_to_pay = amount - discount
        print("Please Pay: \u20b9", amount_to_pay)

    else:
        print("Invalid Promo Code")
        print("Please Pay: \u20b9", amount)

else:
    print("You cannot Apply Promo Code...")
"""

# Ladder if/else

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


# Assignment: You need to suggest the right promo code to
# the user based on the amount which saves the most
