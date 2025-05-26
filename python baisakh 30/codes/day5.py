# Looping Statements
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")
# print("sorry")

# range(stop)
# range(start, stop)
# range(start, stop, step)

# for i in range(10): #[0-9]
#     print("Sorry", i)

# for _ in range(10):  # [0-9]
#     print("Sorry")

# for i in range(1, 10):  # [1-9]
#     print("Sorry", i)


# for i in range(1, 16, 3):  # [1-15, increase by 2]
#     print("Sorry", i)

# # odd numbers from 1-10
# for i in range(1, 10, 2):  # [1-9]
#     print("Odd number ", i)

# even numbers from 1-10
# for i in range(2, 10, 2):  # [1-9]
#     print("Even number ", i)


# even_number = 2
# while even_number < 10:
#     print(even_number)
#     even_number = even_number + 2

# print("End of while loop")


# print multiplication table of 2

# for number in range(1, 11):
#     print(f"2 x {number} = {2 * number}")

# mutiplicand = int(input("Enter a number for multiplication table: "))
# for number in range(1, 11):
#     print(f"{mutiplicand} x {number} = {mutiplicand * number}")


# # multiplication table of 2 and 3
# for number in range(1, 11):
#     print(f"2 x {number} = {2 * number}      3 x {number} = {3 * number}")


# for number in range(1, 11):
#     # if number == 5:
#     #     break
#     if number == 4 or number == 5:
#         continue  # means skip

# for number in range(1, 11):
#     if number == 4 or number == 5:
#         continue  # means skip
#     print(f"2 x {number} = {2 * number}")

# MENU = """
# 1. Day pack
# 2. Voice pack
# 3. Unlimited data
# 4. Exit

# """

# while True:
#     print(MENU)
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         print("Day packs are")
#     elif choice == "2":
#         print("Voice packs are")
#     elif choice == "3":
#         print("Unlimited data packs are")
#     elif choice == "4":
#         print("Thanks for using our service")
#         break
#     else:
#         print("Invalid choice")


# outer loop controls the table no
# inner loop controls the multiplication table


# for table_no in range(1, 31):
#     for number in range(1, 11):
#         print(f"{table_no} x {number} = {table_no * number}")
#     print("****************************************")


