# Multi Value Container

# TUPLE
# Tuples are indexed
# Tuples are IMMUTABLE
# names = "john", "jennie", "jim", "jack", "joe"
names = ("john", "jennie", "jim", "jack", "joe")
print(names)
print(names[2])
# names[2] = "fionna" # error
# del names[1]

print(id(names))
print(id(names[0]))

instagram_user_name = "john"
print(instagram_user_name, id(instagram_user_name))

print(instagram_user_name == names[0])