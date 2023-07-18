# args and kwargs

# *args -> multiple/variable arguments can be passed as TUPLE
def add(*args):
    print(args)
    print(type(args))


add(10, 20)
add(10, 20, 30, 40, 50, 60)
add(10, 20, 30, 40)
add(10.22, 20.33, 30.44, 40.55)


# **kwargs -> key word arguments
def employee_details(**kwargs):
    print(kwargs)
    print(type(kwargs))


employee_details(name="John", age=20, gender="MALE")


def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 20, 30, "john", "sia", name="harry", age=30)