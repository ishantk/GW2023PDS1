names = "John, Jennie, Jim, Jack, Joe"
# Indexing, Neg Indexing, Slicing, Multiplicity, Concatenation, Membership Testing
print(names[1])
print(names[-1])
print(names[1:5])

new_names = names * 2
print(new_names)

print(names, id(names))
names = names + ", Kia"
print(names, id(names))

print("Kia" in names)
print("George" not in names)

