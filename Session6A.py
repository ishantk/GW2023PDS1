# STANDARDIZATION IN OOPS :)

# Object and Attributes: Dish: name, price, ratings
class Dish:
    # CONSTRUCTOR
    def __init__(self, name="", price=0, ratings=4.0):
        self.name = name
        self.price = price
        self.ratings = ratings

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("NAME:", self.name)
        print("PRICE:", self.price)
        print("RATINGS:", self.ratings)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")


dish1 = Dish("Noodles", 300, 4.5)
dish2 = Dish("Burger", 100, 4.3)
dish3 = Dish(name="Fries")

# print(vars(dish1))
# print(vars(dish2))
# print(vars(dish3))

dish1.show()
dish2.show()
dish3.show()

"""
# dish1 and dish2 are reference vars
# they contain hashcode of objects :)
dish1 = Dish()
dish2 = Dish()

dish1.name = "Veggie Burger"
dish1.price = 100
dish1.ratings = 4.3

dish2.name = "Noodles"
dish2.pricing = 300
dish2.rating = 4.5
"""