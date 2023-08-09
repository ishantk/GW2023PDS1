# file = open("ipl-data-2022.csv", "r")
#
# # List of Strings
# lines = file.readlines()
#
# for line in lines:
#     print(line)


with open("ipl-data-2022.csv", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

