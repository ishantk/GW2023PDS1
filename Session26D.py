def upgrade_to_meal(func):

    def inner(amount, taxes, meal_plan):

        if meal_plan == 1:
            print("Upgrading to Medium Meal..")
            print("+ Added Coke")
            print("+ Added Fries")
            amount += 100
            taxes = 0.10

        elif meal_plan == 2:
            print("Upgrading to Large Meal..")
            print("+ Added Large Coke")
            print("+ Added Large Fries")
            print("+ Added Ice Cream")
            amount += 200
            taxes = 0.20
        else:
            print("Thank You for your Purchase..")

        return func(amount, taxes, meal_plan)

    return inner


@upgrade_to_meal
def buy_burger(amount, taxes, meal_plan=0):
    return amount + (amount*taxes)


amount_to_pay = buy_burger(100, 0.10, 0)
print("Mc Donald's Final Charge:", amount_to_pay)