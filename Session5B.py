# Functions in Memory
# Passing References :)
def square(numbers):
    print("[square] numbers is:", numbers, id(numbers))

    for idx in range(len(numbers)): # idx: 0, 1, 2, 3, 4
        numbers[idx] **= 2

    print("[square] numbers now is:", numbers, id(numbers))


def main():
    data = [10, 20, 30, 40, 50]
    print("[main] data is:", data, id(data))
    square(data)
    print("[main] data now is:", data, id(data))


if __name__ == "__main__":
    main()