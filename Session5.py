"""
    Whatever, we write in the py file, is executed by main thread

"""

def main(): # main thread :)
    a = 10
    b = 2*a
    print("b is:", b)

    print("NAME:", __name__)


if __name__ == "__main__":
    main()