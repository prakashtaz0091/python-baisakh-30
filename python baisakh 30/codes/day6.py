# for i in range(1, 5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Loop completed without any errors or breaks")


# def show_table_2():  # function defination
#     for number in range(1, 11):
#         print(f"2 x {number} = {2 * number}")


# # function call or calling a function
# show_table_2()
# show_table_2()


# def show_table(num):  # function defination , num -> parameter
#     for number in range(1, 11):
#         print(f"{num} x {number} = {num * number}")


# # # # function call or calling a function
# show_table(31)  # arguments
# num = int(input("For what number do you want to print the table: "))
# show_table(num)


# def multiplication_table(start, upto):
#     for table_no in range(start, upto + 1):
#         for number in range(1, 11):
#             print(f"{table_no} x {number} = {table_no * number}")
#         print("****************************************")

#         choice = input("q to quit: ")
#         if choice.lower() == "q":
#             break


# multiplication_table(2, 5)


# def example(name, age):
#     print(f"{name} is {age} years old")


# # example("hari", 5)
# example(age=5, name="hari")  # here, age and name are keyword arguments


# def add(*numbers): # here, *numbers is a tuple, it can take any number of arguments
#     print(numbers)


# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# def show_names(**names):
#     print(names)


# show_names(name1="ram", name2="shyam", name3="hari")

"""
here, greeting_keyword is a default argument
"""


def greet(greeting_keyword="Hello !", name="Guest"):
    print(f"{greeting_keyword}, {name}")


greet()

# name = input("Enter your name: ")
# greet(name, "Good Morning")

# greeting_keyword = "Hello !"
# # greeting_keyword = "Good Morning"

# print(greeting_keyword)
