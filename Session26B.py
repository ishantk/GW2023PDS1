# Nested/Local Functions
# create function inside the other function

def outer():
    print("This is outer function")

    def inner(): # nested/local function
        print("This is inner function")

    print("inner is:", inner)
    # inner()
    return inner


result = outer()
print("result is:", result)
result()
