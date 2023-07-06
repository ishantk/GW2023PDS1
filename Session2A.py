# Multi Value Container

# LIST
# LIST is indexed
# LIST is MUTABLE
names = ["john", "jennie", "jim", "jack", "joe"]
print(names)
print(names[2])
names[2] = "fionna" # OK
print(names)
del names[1]
print(names)

names.append("george")
names.append("george")
print(names)