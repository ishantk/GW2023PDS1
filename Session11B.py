# Explore Dictionary
# my_tuple = ()
my_tuple = tuple()
print(my_tuple, type(my_tuple))

# my_list = []
my_list = list()
print(my_list, type(my_list))

my_set = set()
print(my_set, type(my_set))

# my_dictionary = {}
my_dictionary = dict()
print(my_dictionary, type(my_dictionary))

my_data = {101: "John", 201: "Fionna", 301: "George", 661: "Harry"}
print("my_data")
print(my_data)

print("Min:", min(my_data))
print("Max:", max(my_data))
print("Sum:", sum(my_data))

print(my_data[201])
print(my_data.get(201))

# del my_data[201]
my_data.pop(201)
print(my_data)

my_data[775] = "Leo"
print(my_data)

my_data[775] = "Kim"
print(my_data)

del my_data[775]

columns = ["ludhiana", "ferozpur", "moga", "jalandhar", "bathinda"]
population = {}.fromkeys(columns, 1200)
print("population", population)

population["ferozpur"] = 3100

# Convert Dictionary into list of tuples :)
items = list(population.items())
print("items")
print(items)
