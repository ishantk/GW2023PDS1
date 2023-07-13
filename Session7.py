# Relationship Mapping
# 1 Restaurant Has 1 Menu
# 1 Menu Has Many Dishes

class Dish:

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~")
        print(self.name, "|", self.price)
        print(self.rating)
        print("~~~~~~~~~~~~~~~~~~~~~")


class Menu:

    def __init__(self, title, num_of_dishes, dishes):
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show(self):
        print("**********************")
        print(self.title, "|", self.num_of_dishes)
        print("**********************")

        for idx in range(len(self.dishes)):
            self.dishes[idx].show()


class Restaurant:

    def __init__(self, name, address, phone, ratings, menu):
        self.name = name
        self.address = address
        self.phone = phone
        self.ratings = ratings
        self.menu = menu

    def show(self):
        print("======================")
        print(self.name, "|", self.ratings)
        print(self.address, "|", self.phone)
        print("======================")

        self.menu.show()

def main():
   dish1 = Dish(name="Dal Makhani", price=350, rating=4.5)
   dish2 = Dish(name="Paneer Do Pyaza", price=450, rating=5.0)
   dish3 = Dish(name="Noodles", price=250, rating=3.8)
   dish4 = Dish(name="Burger", price=100, rating=4.1)
   dish5 = Dish(name="Fries", price=90, rating=4.8)

   # List of Objects :)
   dishes = [Dish(name="Dal Makhani", price=350, rating=4.5), dish2, dish3, dish4, dish5]

   menu = Menu(title="Indian Delight", num_of_dishes=len(dishes), dishes=dishes)

   restaurant = Restaurant(name="Maharaja",
                            address="Redwood Shores",
                            phone="+1 4414419908", ratings=4.5, menu=menu)

   restaurant.show()


if __name__ == "__main__":
    main()