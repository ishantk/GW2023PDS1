import datetime

# Function
def show():
    print("This is show")
    print("Today is: ", datetime.datetime.today())

# Reference Copy Operation
hello = show

print("show is:", show)
print("hello is:", hello)

show()
hello()

