
def fetch():
    file = open("ipl-data-2022.csv", "r")
    lines = file.readlines()

    for line in lines:
        yield line


# if a function, yields, it means we get Generator in return
result = fetch()
print("result:", result)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result, "No More Record"))
# print(next(result, "No More Record"))

while True:
    data = next(result, "Nothing")
    print(data)
    if data == "Nothing":
        break

