# Bitwise Operators
# &, |, ^

num1 = 10 # 1010
num2 = 8  # 1000

print("num1 binary:", bin(num1))
print("num2 binary:", bin(num2))

result1 = num1 & num2  # 1000 -> 8
result2 = num1 | num2  # 1010 -> 10
result3 = num1 ^ num2  # 0010 -> 2

print("Result1 is:", result1)
print("Result2 is:", result2)
print("Result3 is:", result3)

# Shift Operators
# >>, <<
num1 = 8
num2 = 2

result1 = num1 >> num2 # 2
# rt shift -> base is always 2
# num1 divide by base power num2

result2 = num1 << num2 # 32
result3 = result2 >> num2

print("Result1 is:", result1)
print("Result2 is:", result2)
print("Result3 is:", result3)

num3 = -11
result4 = num3 >> 2
print("Result4 is:", result4)

# binary of 11 -> 1 0 1 1
#                 _ _ 1 0 -> 0 0 1 0 -> 2 :)

# 1 0 1 1
# 0 1 0 0   1s complement
#       1   2s complement

# 0 1 0 1   >> 2
# _ _ 0 1  -> 1 1 0 1
#             0 0 1 0
#                   1
#             0 0 1 1 -> -3

"""
 13 -> 1 1 0 1
       0 0 1 0
             1
       0 0 1 1
       
       0 0 1 1 >> 3
       _ _ _ 0
       
       1 1 1 0
       0 0 0 1 
             1
       0 0 1 0 -> -2             
       

"""

print("-13 >> 3 is:", (-13 >> 3))