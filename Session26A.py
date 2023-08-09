# Function as Input
# i.e. passing the function by reference
def show(func):
    print("Show Executed")
    func()


def hello():
    print("This is hello")
    print("Hello function finished...")


def bye():
    print("This is bye")
    print("bye function finished")


show(hello)
print("````````````````")
show(bye)