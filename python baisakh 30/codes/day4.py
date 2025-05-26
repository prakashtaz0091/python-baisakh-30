"""
Today we are exploring control flow statements
"""

# 1. Conditional Statement
# 1.a. if statement
# 1.b. if-else statement
# user_age = int(input("Enter your age: "))

# if user_age >= 18:
#     print("You can apply for citizenship card")
#     print("Please visit office with your birth certificate and parents")
# else:  # else means otherwise
#     print("You cannot apply for citizenship card")
#     print("Your current age is not enough to apply for citizenship card")

# 1.c. if-elif...else statement
# marks = int(input("Enter marks obtained: "))
# if marks > 100 or marks < 0:
#     print("Invalid marks")
# elif marks >= 90:
#     print("Your grade is A+")
# elif marks >= 80:
#     print("Your grade is A")
# elif marks >= 70:
#     print("Your grade is B+")
# elif marks >= 60:
#     print("Your grade is B")
# elif marks >= 50:
#     print("Your grade is C+")
# elif marks >= 40:
#     print("Your grade is C")
# elif marks >= 0 and marks < 40:
#     print("Your grade is NG")

# Nested conditional statements
# user_age = int(input("Enter your age: "))
# user_gender = input("Enter your gender (male/female) : ")

# if user_gender == "male":
#     if user_age >= 18:
#         print("You can apply for citizenship card")
#         print("Please visit office with your birth certificate and parents")
#     else:
#         print("You cannot apply for citizenship card")
#         print("Your current age is not enough to apply for citizenship card")
# elif user_gender == "female":
#     if user_age >= 16:
#         print("You can apply for citizenship card")
#         print("Please visit office with your birth certificate and parents")
#     else:
#         print("You cannot apply for citizenship card")
#         print("Your current age is not enough to apply for citizenship card")
# else:
#     print("Invalid gender")

# without using nested conditional,
# user_age = int(input("Enter your age: "))
# user_gender = input("Enter your gender (male/female) : ")

# if (user_gender == "male" and user_age >= 18) or (
#     user_gender == "female" and user_age >= 16
# ):
#     print("You can apply for citizenship card")
#     print("Please visit office with your birth certificate and parents")
# else:
#     print("You cannot apply for citizenship card")
#     print("Your current age is not enough to apply for citizenship card")


# (HW)Improve above program to handle invalid age and gender

# or logical operation
science_marks = int(input("Enter science marks: "))
maths_marks = int(input("Enter maths marks: "))
english_marks = int(input("Enter english marks: "))

# if science_marks < 40 or maths_marks < 40 or english_marks < 40:
#     print("Failed the exam")
# else:
#     print("Passed the exam")


# and operation
if science_marks >= 40 and maths_marks >= 40 and english_marks >= 40:
    print("Passed the exam")
else:
    print("Failed the exam")
