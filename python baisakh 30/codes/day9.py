# Problem statement: This program doesn't remembers the student records after the program is closed
# For Example:

# students = []  # dummy database

# while True:
#     student_name = input("Enter student name (q to quit): ")
#     if student_name == "q":
#         break
#     students.append(student_name)


# print("################################")
# print("Student Records:")
# for student in students:
#     print(student)


# To solve above problem we use the concept of file handling
# with open("student_records.txt", "a") as file:
#     while True:
#         student_name = input("Enter student name (q to quit): ")
#         if student_name == "q":
#             break
#         file.write(f"{student_name}\n")


# with open("student_records.txt", "r") as file:
#     content = file.readlines()
#     # print(content)
#     # print(type(content))
#     for line in content:
#         print(line.strip())


# search_name = input("Student name to search: ")
# found = False
# with open("student_records.txt", "r") as file:
#     content = file.readlines()
#     # content = ["ram\n", "hari\n", "shrawan\n", "roshan\n"]
#     for name in content:
#         cleaned_name = name.strip()
#         if cleaned_name == search_name:
#             print("Found the student")
#             found = True
#             break

# #  not False -> True
# if not found:
#     print("The record you are searching for doesn't exist")


# "ram" in ["ram", "hari", "shrawan"]

# search_name = input("Student name to search: ")
# search_name_with_newline = search_name + "\n"  # search_name = "ram\n"
# found = False

# with open("student_records.txt", "r") as file:
#     content = file.readlines()
#     if search_name_with_newline in content:
#         print("Found the student")
#         found = True


# #  not False -> True
# if not found:
#     print("The record you are searching for doesn't exist")


# with open("student_records.txt", "w") as file:
#     while True:
#         student_name = input("Enter student name (q to quit): ")
#         if student_name == "q":
#             break
#         file.write(f"{student_name}\n")

# import csv

# with open("student_records.csv", "a") as file:
#     new_records = []
#     while True:
#         student_name = input("Enter student name: ")
#         student_roll_no = input("Enter student roll_no: ")
#         student_address = input("Enter student address: ")

#         writer = csv.writer(file)
#         writer.writerow([student_name, student_roll_no, student_address])
#         writer.writerows()

#         choice = input("Do you want to add another student record (y/n): ")
#         if choice == "n":
#             break


# with open("student_records.csv", "a") as file:
#     new_records = []
#     while True:
#         student_name = input("Enter student name: ")
#         student_roll_no = input("Enter student roll_no: ")
#         student_address = input("Enter student address: ")

#         new_single_student_record = [student_name, student_roll_no, student_address]

#         new_records.append(new_single_student_record)

#         choice = input("Do you want to add another student record (y/n): ")
#         if choice == "n":
#             break

#     writer = csv.writer(file)
#     writer.writerows(new_records)
