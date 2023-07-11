# RECURSION :)

def get_max(numbers, length):
    if length == 1:
        return numbers[0]
    else:
        result = get_max(numbers, length-1)
        if result > numbers[length-1]:
            return result
        else:
            return numbers[length-1]


def main():
    data = [20, 30, 10]
    max_number = get_max(data, len(data))
    print("MAX NUMBER:", max_number)


if __name__ == "__main__":
    main()


# Assignment:
# Fibonaccie Series :)
# 0 1 1 2 3 5 8 ....