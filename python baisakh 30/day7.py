# Data Structures
# List -> mutable
# Tuple -> immutable
# Set -> mutable
# Dictionary -> mutable

# 1. List
# numbers = [1, 2, 4]
# fruits = ["apple", "banana", "cherry"]
# data = [1, "apple", 3.114, True, None]
# shopping_list = ["apple", "banana", "shoes", "mobile"]

# print(shopping_list[-2])
# first_item = shopping_list[1]  # getting data from list
# shopping_list[1] = "grapes"  # updating data in specific index
# # first_item = "grapes"


# print(shopping_list)

# volleyball_team = ["ram", "shyam"]
# print(volleyball_team)

# volleyball_team.append("hari")  # add to last/end
# print(volleyball_team)

# volleyball_team.append("ramesh")  # add to last/end
# print(volleyball_team)

# volleyball_team.pop()  # remove from last/end
# print(volleyball_team)

# volleyball_team.pop(2) # remove from specific index
# print(volleyball_team)

# volleyball_team.insert(1, "gaurav")  # add data to specific index
# print(volleyball_team)

# volleyball_team.remove("ram")  # remove data from list using value
# print(volleyball_team)

# using for loop to access all data in list, one by one
# for player in volleyball_team:
#     print(player)

# using for loop to access all data in list, one by one with a numbering
# for number, player in enumerate(volleyball_team, start=1):
#     print(number, player)

# print(len("password]"))

# player_nos = [7, 9, 10, 2]
# player_names = ["ram", "shyam", "hari", "gaurav"]
# print(len(player_names))
# for data in zip(player_nos, player_names):
#     print(data)
# for player_no, player_name in zip(player_nos, player_names):
#     print(player_no, player_name)


# class_10_dance_list = ["ram", "seeta", "geeta"]
# class_9_dance_list = ["hari", "shyam", "gaurav"]
# all_dance_candidates = class_10_dance_list + class_9_dance_list

# print(all_dance_candidates)
# print(class_10_dance_list * 2)


# Tuple
# final_dance_list = tuple(all_dance_candidates)
# final_dance_list.remove("gaurav")
# print(final_dance_list)


# where tuple is used by python itself
# def add(*numbers):  # here, *numbers is a tuple, it can take any number of arguments
#     result = 0
#     for number in numbers:
#         result += number
#     print(result)


# add(1, 2, 3, 4, 5234234, 6, 7, 8, 9, 10)

# days_of_week = (
#     "sunday",
#     "monday",
#     "tuesday",
#     "wednesday",
#     "thursday",
#     "friday",
#     "saturday",
# )
# print(days_of_week[-1])
# days_of_week_list = list(days_of_week)
# days_of_week_list.append("Extra day")
# days_of_week = tuple(days_of_week_list)
# print(days_of_week)
