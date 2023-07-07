# Operators

# Arithmetic Operators
# +, -, *, **, /, //, %

product_price = 125.25
taxes = 0.18

# Associativity and Precedence (Self Read :))
price_to_pay = product_price + (product_price * taxes)
print("Price to Pay: \u20b9", price_to_pay)

number = 10
# result = number/3     # Floating Point Div
result = number // 3    # Integral Div
print("Result:", result) # 3

base = 2
# result = result * 2
result = base ** result
print("Result:", result) # 8


# Assignment Operators
# =, +=, -=, *=, **=, /=, //=, %=

age = 20
# age = age + 3
age += 3  # age = age + 3
age += 10
age -= 5
age %= 3

print("Age is:", age)

# Increment and Decrement Operators
# ++ and -- does not exist in Python

idx = 0
idx += 3
idx -= 1
print("idx is:", idx)