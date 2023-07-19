# For Each or Enhanced For Loop

data = list(range(10, 101, 10))
print("data:", data)

"""
for idx in range(len(data)):
    print(data[idx])
"""

data = set(data)

# element can be any name of your choice
# Work for list tuple, set :)
for element in data:
    print(element)

student = {
    "rollno": 101,
    "name": "Fionna",
    "age": 21
}
print("Dictionary Data...")

items = student.items()
for item in items:
    # print(item)
    print(item[0], item[1])

print("Dictionary Keys Only...")
keys = student.keys()
for key in keys:
    print(key)

print("Dictionary Key and Values")
for key in student:
    print(key, student[key])