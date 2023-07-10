"""
    Another Brick in the Wall :)

    john: 1 2 3...
    jack: 2 4 6...

    total: 12 + 1 -> 13
           jack: 1

    total bricks: 13

"""

total_bricks = int(input("Enter Number of Bricks: "))
bricks_in_wall = 0

for idx in range(1, total_bricks):
    john_bricks = idx
    bricks_in_wall += john_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print("John Placed the Last Brick:", (john_bricks - difference))
        break

    jack_bricks = idx * 2
    bricks_in_wall += jack_bricks

    if bricks_in_wall >= total_bricks:
        difference = bricks_in_wall - total_bricks
        print("Jack Placed the Last Brick:", (jack_bricks-difference))
        break


print("bricks_in_wall is:", (bricks_in_wall-difference))

# Solve the same problem using while loop :)

