# CASE STUDY
# ZOMATO with Python Storage Containers

promo_codes = ["WELCOME 50", "ZOMPAYTM", "BINGO", "JUMBO"]

dish1 = {
    "name": "Mc Aloo Tikki",
    "price": 100,
    "ratings": 4.3
}

dish2 = {
    "name": "Mc Veggie",
    "price": 140,
    "ratings": 4.7
}

dish3 = {
    "name": "Mc Veggie Wrap",
    "price": 80,
    "ratings": 3.5
}

menu = [dish1, dish2, dish3, {"name": "Mc Egg", "price": 75, "ratings": 4.1}]

restaurant = {
    "name": "Mc Donalds",
    "address": "Ansla Plaza, Ludhiana",
    "description": "Burger, Fast Food, Coffee, Beverages, Wraps",
    "ratings": 4.5,
    "menu": menu,
    "promos": promo_codes
}