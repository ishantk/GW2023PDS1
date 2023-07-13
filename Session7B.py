"""
    1 Menu has many Options
    1 Option has Many Categories
    Many Categories has Many Products

"""


class Menu:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def show(self):
        print(self.name, end=" | ")

    def show_categories(self):
        for idx in range(len(self.categories)):
            self.categories[idx].show()



class Product:

    def __init__(self, name, brand, price, rating):
        self.name = name
        self.brand = brand
        self.price = price
        self.rating = rating

    def show(self):
        print("-----------------------")
        print(self.name, " | ", self.brand)
        print(self.price, " | ", self.rating)
        print("-----------------------")


class Category:

    def __init__(self, title, num_of_products, min_discount, products):
        self.title = title
        self.num_of_products = num_of_products
        self.min_discount = min_discount
        self.products = products

    def show(self):
        print("************************")
        print(self.title, " | ", self.num_of_products)
        print(self.min_discount)
        print("************************")

    def show_products(self):
        for idx in range(len(self.products)):
            self.products[idx].show()

