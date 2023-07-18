"""
    Multi Value Containers
        Sequences:
            Tuple
            List
            Set
            String

        Dictionary

    Properties:
        1. Indexing
        2. Negative Indexing
        3. Slicing
        4. Concatenation
        5. Multiplicity
        6. Membership Testing

"""

# 1D List
#           0   1   2
#          -3  -2  -1
my_data = [10, 20, 30]
# my_data = (10, 20, 30)

# 2D List
numbers = [
    [10, 20, 30],
    [40, 50, 60, 70, 80],
    [90, 99]
]

# List of List of Lists
# 3D List
large_data = [
    [
        [10, 20, 30],
        [40, 50, 60, 70, 80],
        [90, 99]
    ],
    [
        [10, 20, 30],
        [40, 50, 60, 70, 80],
        [90, 99]
    ]
]

# 1. Indexing
print(len(my_data))
print(my_data[1])

print(len(numbers)) # 3
print(numbers[1])   # entire list
print(numbers[1][2]) # 60
print(large_data[1][2][0]) # 90s

print(my_data[-1]) # 30
print(numbers[-2][-1])

# Slicing
data = list(range(10, 101, 10))
print("data:", data)
print("data[:5]", data[:5]) # print(data[0:5])
print("data[6:]", data[6:])
print("data[5:9]", data[5:9])

print("data[:-5]", data[:-5])
print("data[-5:-2]", data[-5:-2])

# Concatenation
data1 = [10, 20, 30]
data2 = [40, 50, 60]

data3 = data1 + data2
print("data3:", data3)

# Multiplicity
data4 = data1 * 2
print("data4 is:", data4)

# Membership Testing
print(10 in data1)
print(100 in data1)
print(100 not in data1)

student = {
    "name": "John Watson",
    "age": 30,
    "gender": "male",
    "rollno": 101,
    "address": "Resdwood Shores"
}

print(student["name"])
print("rollno" in student)


# Assignment -> Explore all the properties on String :)
quote = "Search the Candle rather than cursing the darkness"
print(quote[6])