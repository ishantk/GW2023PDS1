# Multi Value Container

# SET
# Output is UNORDERED
# It does not support INDEXING
# It works on Hashing
john_followers = {"fionna", "jack", "harry", "sia", "kim", "jack"}
print(john_followers, type(john_followers), id(john_followers))

fionna_followers = {"leo", "nab", "harry", "ben", "kim"}
print(fionna_followers, type(fionna_followers), id(fionna_followers))

mutual_followers = john_followers.intersection(fionna_followers)
print(mutual_followers, type(mutual_followers), id(mutual_followers))

mutual_list = list(mutual_followers)
print(mutual_list, type(mutual_list), id(mutual_list))

