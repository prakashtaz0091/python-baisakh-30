# def deco_func(func):
#     def wrapper_func(*args, **kwargs):
#         print("This is before function execution")
#         func(*args, **kwargs)
#         print("This is after function execution")

#     return wrapper_func


# @deco_func
# def example():
#     print("This is example function")


# @deco_func
# def example2():
#     print("This is example2 function")


# # example()
# example2()


# def login_required(func):
#     def wrapper_func(*args, **kwargs):
#         logged_in = False
#         if logged_in:
#             func(*args, **kwargs)
#         else:
#             login_view()

#     return wrapper_func


# def login_view():
#     print("Login page")

# @login_required
# # @admin_required
# def home_view():
#     print("Home page")

# @login_required
# def home_view():
#     print("Home page")


# @login_required
# def contact_view():
#     print("Contact page")


# home_view()
# contact_view()


# l1 = [1, 2, 3]
# l2 = []

# for number in l1:
#     result = number**2
#     l2.append(result)

# print(l1)
# print(l2)
# def func(a, b):
#     print(a, b)

#     return a + b


# l1 = [1, 2, 3]
# l2 = list(map(lambda number: number**2, l1))

# print(l1)
# print(l2)


# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# l4 = [6, 7, 8]
# add_of_l1_l2 = list(map(lambda a, b, c: a + b + c, l1, l2, l4))
# print(add_of_l1_l2)

#
# numbers = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
#     10,
# ]


# numbers_gt_5 = list(filter(lambda number: number > 5, numbers))
# print(numbers_gt_5)
# odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))
# print(odd_numbers)


# Generator (yield instead of return)
# def number_generator():
#     yield 1
#     yield 2
#     yield 3


# numbers = number_generator()
# print(next(numbers))  # 1
# print(next(numbers))  # 2
# print(next(numbers))  # 3
# print(next(numbers))  # StopIteration


# infinite numbers
# def number_generator():
#     number = 2
#     while True:
#         yield number  # 3
#         number = number + 2


# number = number_generator()
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# for num in number: # for loop runs infinitely
#     print(num)

# for _ in range(10):
#     print(next(number))


# def dictionary_attack(file_name):
#     with open(file_name) as file:
#         for line in file:
#             yield line.strip()


# password = dictionary_attack("passwords.txt")


# password_to_crack = "pr@k@$h@123"
# while True:
#     try_password = next(password)
#     if try_password == password_to_crack:
#         print(f"Password is {try_password}")
#         break
#     else:
#         print(f"Trying {try_password}")
