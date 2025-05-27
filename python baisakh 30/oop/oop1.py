# class = 10
# Age =
# ram_age


# class Student:
#     pass


# s1 = Student()
# s1.name = "ram"
# s1.age = 10
# # print(type(s1))
# # print(s1.name)
# # print(s1.age)
# print(f"{s1.name} is {s1.age} years old")


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# s1 = Student("ram", 10)
# print(f"{s1.name} is {s1.age} years old")


class Mobile:
    def __init__(
        self, name, price, brand="no_brand", battery_capacity=""
    ):  # constructor
        self.name = name
        self.price = price
        self.model_no = ""
        self.brand = brand
        self.battery_capacity = battery_capacity
        self.storage_capacity = ""


# samsung_s24_ultra = Mobile("samsung_s24_ultra", 100000, "samsung")
# samsung_s24_ultra = Mobile("samsung_s24_ultra", 100000, battery_capacity="5000mAh")
# # samsung_s24_ultra.brand = "samsung"
# print(samsung_s24_ultra.name)
# print(samsung_s24_ultra.price)
# print(samsung_s24_ultra.brand)


# iphone_16_pro_max = Mobile("iphone_16_pro_max", 120000)
# iphone_16_pro_max.brand = "apple"
# print(iphone_16_pro_max.name)
# print(iphone_16_pro_max.price)
# print(iphone_16_pro_max.brand)


mobiles = []  # objects of class Mobile

MENU = """
1. Add new mobile info
2. View all mobile info
3. Update mobile info
4. Exit
"""


def add_mobile_info():
    mobile_name = input("Mobile name: ")
    mobile_price = float(input("Mobile price: "))

    new_info = Mobile(mobile_name, mobile_price)
    mobiles.append(new_info)


def view_all_mobile_info():
    for mobile_info in mobiles:
        print("Mobile name:", mobile_info.name)
        print("Mobile price:", mobile_info.price)
        print("Mobile brand:", mobile_info.brand)
        print("Mobile model no:", mobile_info.model_no)
        print("Mobile storage capacity:", mobile_info.storage_capacity)
        print("Mobile battery capacity:", mobile_info.battery_capacity)
        print("##############################")


def update_mobile_info():
    to_be_updated_name = input("Enter name of mobile to be updated: ")

    # intially set mobile_info_to_be_updated to None
    mobile_info_to_be_updated = None

    # search for the mobile to be updated
    for mobile_info in mobiles:
        if mobile_info.name == to_be_updated_name:
            mobile_info_to_be_updated = mobile_info
            break

    if mobile_info_to_be_updated is not None:
        print("Mobile to be updated found")

        property_to_be_updated = input("""
                                       Enter the property to be updated:
                                       ---Options---
                                       price
                                       brand
                                       battery_capacity
                                       storage_capacity
                                       """)
        new_value = input(f"New {property_to_be_updated}: ")

        setattr(mobile_info_to_be_updated, property_to_be_updated, new_value)
        print("Mobile info updated successfully")

    else:
        print("Mobile to be updated not found")


while True:
    print(MENU)

    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        add_mobile_info()

    elif menu_choice == "2":
        view_all_mobile_info()

    elif menu_choice == "3":
        update_mobile_info()

    elif menu_choice == "4":
        print("Thanks for using the application")
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# range(10) -> [0-9]
# range(1, 101) -> [0-9]
