# Break and Continue :)

# floor_number = int(input("Enter Floor Number: "))
#
# for floor in range(1, 11):
#     print("Elevator Arrived on Floor#", floor)
#
#     if floor == floor_number:
#         break

for idx in range(1, 11):

    # if idx >= 5:
    #     print("Idx is:", idx)

    if idx <= 5:
        continue

    print("Idx is:", idx)