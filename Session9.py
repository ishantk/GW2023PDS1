def compute_taxes(amount=100, tax=0.18):
    amount_to_pay = amount + amount*tax
    return amount_to_pay


# Printing the hash code of function
print("compute_taxes is:", compute_taxes)
print("compute_taxes hashcode is:", id(compute_taxes), hex(id(compute_taxes)))

# REFERENCE COPY :)
fun = compute_taxes
print("fun is:", fun)

result = fun()
print("Result is:", result)

result = fun(100, 25)
result = fun(tax=25, amount=100)
result = fun(amount=100, tax=0.18)
print("Result is:", result)

# del compute_taxes

# result = fun(amount=200, tax=0.18)
# print("Result is:", result)