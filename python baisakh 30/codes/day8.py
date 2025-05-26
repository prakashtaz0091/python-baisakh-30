# Set
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1 = {1, 2, 3, 4, 4, 2, 3, 2}
# s2 = {2, 3, 4, 5}

# print(type(s1)) # check the type of s1
# print(s1)
# print(s2)

# teacher1_dance_list = ["ram", "shyam", "hari"]
# teacher2_dance_list = ["ram", "seeta", "geeta"]
# final_dance_list = teacher1_dance_list + teacher2_dance_list
# # print("final_dance_list", final_dance_list)

# unique_final_dance_list_set = set(final_dance_list)
# print("unique_final_dance_list", unique_final_dance_list_set)
# print(unique_final_dance_list_set[0]) # wrong, cannot access set values by index

# for dancer in unique_final_dance_list_set:
#     print(dancer)


# ram_hobbies = {"playing", "singing", "dancing"}
hari_hobbies = {"playing", "singing", "travelling"}

# common_hobbies = ram_hobbies.intersection(hari_hobbies)
# common_hobbies = ram_hobbies & hari_hobbies
# print(common_hobbies)


# all_hobbies = ram_hobbies.union(hari_hobbies)
# all_hobbies = ram_hobbies | hari_hobbies
# print(all_hobbies)

# ram_hobbies_only = ram_hobbies.difference(hari_hobbies)
# ram_hobbies_only = ram_hobbies - hari_hobbies
# print(ram_hobbies_only)

# hari_hobbies_only = hari_hobbies - ram_hobbies
# print(hari_hobbies_only)


# Symmetric difference is the combination of results of A-B and B-A, where A and B are sets
# sym_diff = ram_hobbies.symmetric_difference(hari_hobbies)
# sym_diff = ram_hobbies ^ hari_hobbies
# print(sym_diff)


# hari_hobbies.update(["reading", "writing"]) # add multiple values
# print(hari_hobbies)

# hari_hobbies.remove("singing") # remove by value
# try:
#     hari_hobbies.remove("reading")
# except KeyError as e:
#     print(e)


# print(hari_hobbies)
# prin()


# hobbies = set()

# while True:
#     hobby = input("Enter a hobby ('exit' to stop adding hobbies): ")
#     if hobby == "exit":
#         break
#     hobbies.add(hobby)

# print(hobbies)

# while True:
#     remove_hobby = input("Enter a hobby that you want to remove: ")
#     try:
#         hobbies.remove(remove_hobby)
#     except KeyError as e:
#         print(f"{e} doesn't exist")

#     print(hobbies)

# person = ["ram", 20, "ABC College", "Kathmandu", "1234567890"]
# person = {
#     "name": "ram",
#     "age": 20,
#     "college": "ABC College",
#     "address": "Kathmandu",
#     "phone": "1234567890",
#     # "bike": "Dominar",
# }

# print(person["name"])  # access by key
# print(person["age"]) # access by key
# print(person["college"]) # access by key
# print(person["bike"])  # access by key, but gives key error and breaks the program
# print(person.keys())  # get all keys
# print("name" in person.keys())  # check if key exists
# print("bike" in person.keys())  # check if key exists
# if "bike" in person.keys():
#     print("bike exists")
#     print("bike is", person["bike"])
# else:
#     print("bike doesn't exist")

# print(person.values())
# print(person.items())

# for item in person.items():
#     print("key", item[0])
#     print("value", item[1])

# unpacking
# a, b = (1, 2)
# a, b = [1, 2]
# a, b = {1, 2}
# print(a)
# print(b)

# key, value = ("name", "ram")
# print(key)
# print(value)
# number, name = (1, "ram")

# for key, value in person.items():
#     print(key, value)

# print(person)
# # person["age"] = 21
# # person["bike"] = "Dominar"
# # del person["age"]
# # del person["bike"]
# # removed_item = person.pop("age")
# # removed_item = person.popitem()

# # print("removed item", removed_item)
# print(person)


# person = {
#     "name": "ram",
#     "age": 20,
#     "college": {
#         "name": "ABC College",
#         "location": "Kathmandu",
#         "faculty": {
#             "name": "Computer Science",
#             "department": {
#                 "head": "Prof. Shyam",
#                 "assistant": "Prof. Hari",
#             },
#         },
#         "course": {
#             "name": "BSc.CSIT",
#             "course_code": "CSC1001",
#             "course_duration": "4 years",
#         },
#     },
#     "address": {
#         "temporary": "Kathmandu",
#         "permanent": {
#             "city": "Birtamode",
#             "zipcode": "44600",
#             "galli_name": "A",
#             "house_no": "101",
#         },
#     },
#     "phone": {
#         "home": "1234567890",
#         "office": "9876543210",
#     },
#     "hobbies": ["playing", "singing", "dancing"],
# }

# address = person["address"]
# print(address["temporary"])
# print(address["permanent"])
# print(person["address"]["temporary"])
# print(person["address"]["permanent"]["house_no"])
# print(person["address"]["permanent"]["galli_name"])
# print(person.keys())
# print(person["college"]["faculty"]["department"].keys())
# print(person["college"]["faculty"]["department"]["head"])
