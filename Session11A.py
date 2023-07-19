# Explore Set
# UNIQUE

john_followers = {"fionna", "sia", "jack", "joe", "george"}
print(john_followers, type(john_followers))

numbers = list(range(10, 101, 10))
print(numbers, type(numbers))

numbers = set(numbers)
print("numbers now:", numbers)
print("numbers type:", type(numbers))

numbers.add(10)
numbers.add(110)
numbers.add(20)
numbers.add(220)

print("numbers after add:", numbers)
numbers.pop()
numbers.pop()
print("numbers after pop:", numbers)

numbers.remove(50)
numbers.discard(30)
numbers.discard(90)
print("numbers after remove:", numbers)

john_followers = {"fionna", "sia", "jack", "joe", "george"}
jake_followers = {"anna", "jack", "leo", "joe", "harry", "mike"}
fionna_followers = {"sia", "joe"}

print("john_followers:", john_followers)
print("jake_followers:", jake_followers)
print("fionna_followers:", fionna_followers)

followers = john_followers.intersection(jake_followers)
followers = john_followers.intersection(jake_followers).intersection(fionna_followers)
print("followers:", followers)

print("issubset:", fionna_followers.issubset(john_followers))
print("issuperset:", john_followers.issuperset(fionna_followers))

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

C = A - B
print("C is:", C)

D = A & B
print("D is:", D)

E = A ^ B
print("E is:", E)

F = A | B
print("F is:", F)

# Explore what is symmetric_difference
G = A.symmetric_difference(B)
print("G is:", G)

A.clear()
