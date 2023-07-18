# Re Define the Function :)

# V1
def compute_taxes(amount=100, tax=0.18):
    amount_to_pay = amount + amount*tax
    return amount_to_pay

# Save the Old Definition :)
old_compute_taxes = compute_taxes

print("compute_taxes is:", compute_taxes)

# V2
def compute_taxes(amount=100, tax=0.18, extra=0.10):
    amount_to_pay = amount + amount*tax + amount*extra
    return amount_to_pay


print("compute_taxes now is:", compute_taxes)


print(compute_taxes()) # 128


class Dish:
    def __init__(self, name="Burger", price=100):
        self.name = name
        self.price = price

    def __init__(self, name="Noodles", price=200, rating=5.0):
        self.name = name
        self.price = price
        self.rating = rating


dish1 = Dish()
print(vars(dish1))

print(old_compute_taxes())
