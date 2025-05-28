# class Student:
#     school = "lalitpur school"  # class variable/class attribute
#     student_count = 0

#     def __init__(self, name, age, address, class_):  # constructor
#         self.name = name  # self.name is instance variable/attribute
#         self.age = age
#         self.address = address
#         self.class_ = class_

#         Student.student_count += 1

#     def show_info(self):  # instance method
#         print(self.name)
#         print(self.age)
#         print(self.address)
#         print(self.class_)
#         print(self.school)

#     @classmethod
#     def show_school_name(cls):
#         print(f"The name of school is {cls.school}")  # Student.school


# s1 = Student("ram", 10, "kathmandu", "10th")

# # print(s1.name)
# # # print(s1.age)
# # # print(s1.address)
# # # print(s1.class_)
# # print(s1.school)

# s2 = Student("hari", 11, "kathmandu", "11th")

# # print(s2.name)
# # print(s2.school)

# # s1.show_info()
# # s2.show_info()

# # class Str:
# #     def upper(self):
# #         pass

# #     def lower(self):
# #         pass

# # str1 = "ram"
# # str1.upper()

# # print("ram".upper())
# # print("RAM".lower())
# # print(Student.school) # we can access class variable using class name or object both
# # Student.show_school_name()

# # print(Student.student_count)


# access modifiers
# 1. public
# 2. protected  # self._name
# 3. private
class BankAccount:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__balance = 0

    @property  # getter method, usually used for accessing private variable
    def balance(self):
        return self.__balance

    @balance.setter  # setter method, usually used for setting new value to private variable
    def balance(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise TypeError("Balance must be a positive number")
        if new_value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = new_value

    def show_info(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Balance:", self.__balance)


ram_account = BankAccount("ram", "kathmandu")
# print(ram_account.balance)
# ram_account.balance = -1000 # now this will give value error
# ram_account.balance = "laskdfjlskdfjl"
# print(ram_account.balance)

while True:
    try:
        deposit_balance = float(input("Deposit amount: "))
        ram_account.balance = deposit_balance
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print("Depositted successfully")
        ram_account.show_info()
        break

# print(ram_account.balance)
# print(ram_account.__balance)
# print(ram_account._BankAccount__balance)  # name mangling
# ram_account.show_info()
# ram_account.balance = -1000
# ram_account.show_info()
