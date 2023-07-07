# Conditional Operators
# ==, >=, <=, !=, >, <

cab_fare = 500
e_wallet = 500

print("Can i Book the Cab: ", (e_wallet >= cab_fare))
print("Can i Book the Cab: ", (cab_fare <= e_wallet))

email = input("Enter Your Email: ")
password = input("Enter Your Password: ")

print("Email is: ", email, "and password is:", password)
print("Email Login Status: ", (email == "john@example.com"))
print("Password Login Status: ", (password == "john123"))

# Logical Operators: and or

print("Final Login Status: ", ( (email == "john@example.com") and (password == "john123") ) )

otp = 3027
user_otp = int(input("Enter OTP: "))
print("OTP Status:", (otp == user_otp))

# Membership Testing
# is, is not
a = 10
b = 10

print(a is b) # True
print(a == b) # True
print(a is not b) # False

# Assignment: Explore difference between is and ==