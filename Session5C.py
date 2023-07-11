
def print_number(num):
    print(num)
    num += 1

    if num <= 10:
        print_number(num) # Executing a function from a function -> RECURSION


if __name__ == "__main__":
    print_number(1)