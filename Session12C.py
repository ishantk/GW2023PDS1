names = "John, Jennie, Jim, Jack, Joe"
print(len(names)) # 28
print(names[1])   # o
print(names[len(names)-1]) # e

split_names = names.split(", ")
print(split_names, type(split_names))

s1 = names.replace("Jim", "Mike")
print("names:", names)
print("s1:", s1)

idx = names.find("Zee")
print("idx is:", idx)



