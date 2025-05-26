# List comprehension

# l1 = [1, 2, 3, 4, 5, 6]

# # new_list = [num**2 for num in l1]
# new_list = [num for num in l1 if num > 3]

# print(new_list)


# Dictionary Comprehension
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ["one", "two", "three", "four", "five", "six"]

# a, b = (1, "one")
# key, value = (1, "one")
# value, key = (1, "one")

# # {
# #     1:"one",
# #     2:"two",
# #     3:"three",
# #     4:"four",
# #     5:"five",
# #     6:"six"
# # }

# d1 = {num: name for num, name in zip(l1, l2) if num >= 3}
# print(d1)


# d1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"}
# # reverse_key_values = {value: key for key, value in d1.items()}
# # print(reverse_key_values)
# reverse_key_values = {b: a for a, b in d1.items()}
# print(reverse_key_values)


# Generator Comprehension/Expression
# odd_numbers = (num for num in range(1, 11, 2))
# # print(odd_numbers)
# for num in odd_numbers:
#     print(num)

# datetime.py---->datetime--->now()
# ---->others


# import datetime
# from datetime import datetime as samaya

# # now = datetime.datetime.now()  # 2025-05-25 20:53:45.973073
# now = samaya.now()  # 2025-05-25 20:53:45.973073
# # print("now", now)
# hour = now.hour

# if hour < 12:
#     print("Good Morning")
# elif hour < 17:
#     print("Good Afternoon")
# else:
#     print("Good Evening")


# import time
# import os

# for countdown_number in range(10, -1, -1):
#     print(countdown_number)
#     time.sleep(1)
#     if os.name == "posix":
#         os.system("clear")
#     else:
#         os.system("cls")

# print("HAPPY NEW YEAR")
# def func():
# result = #some formula
# return result

import math

# result = math.factorial(5)
# print(result)
# hcf = math.gcd(10, 20, 5)
# print(hcf)
# # int(3.123) -> 3
# print(math.isqrt(10))

# print(math.ceil(3.14))
# print(math.floor(3.14))

# these are built-in functions not the part of math module
# print(round(3.95))
# print(sum([1, 2, 3, 4, 5, 6]))
# print(sum([1, 2, 3, 4, 5, 6], start=10))

# print(math.pi)
