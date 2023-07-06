# A .py file is a python program
# We call it as Python Script
# We can also call it as Module

# Single Value Container

# Create Operation - RAM
instagram_user_name = "auribises"

# Read Operation
print(instagram_user_name, id(instagram_user_name))
print(instagram_user_name, hex(id(instagram_user_name)))
print(instagram_user_name, oct(id(instagram_user_name)))
print(instagram_user_name, bin(id(instagram_user_name)))
print(type(instagram_user_name))

user_name = "k_ishant"
print(user_name, id(user_name), type(user_name))

# user_name is a reference variable which will be created in STACK
# Value k_ishant is created within a storage container of type string in HEAP

user = "k_ishant"
print(user, id(user), type(user))

# REFERENCE COPY Operation
another_user = user
print(another_user, id(another_user), type(another_user))

# UPDATE OPERATION
user = "anaya"
print(user, id(user), type(user))

# DELETE Operation
del user
# print(user, id(user), type(user))  # error

del another_user
# print(another_user, id(another_user), type(another_user))  # error
print(user_name, id(user_name), type(user_name))







