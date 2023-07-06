# Multi Value Container

# Create Operation
numbers = 10, 20, 30, 40, 50

# Read Operation
print(numbers, id(numbers), type(numbers))

# Indexing
#        0   1      2        3      4
# data = (10, 10.2, "hello", "wow", 200)
data = [10, 10.2, "hello", "wow", 200]
print(data, id(data), type(data))

print(data[0], id(data[0]), type(data[0]))
print(data[1], id(data[1]), type(data[1]))
print(data[2], id(data[2]), type(data[2]))

# Reference Copy Operation
my_data = data
print(my_data, id(my_data), type(my_data))
print(my_data[3])

# IMMUTABLE - TUPLE
# MUTABLE - LIST
my_data[2] = "Awesome"

print(my_data, id(my_data), type(my_data))
del my_data[3]
print(my_data)
print(data)


