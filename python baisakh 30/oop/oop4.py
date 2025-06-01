# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

#     def __add__(point1, point2):
#         # print(f"Trying to add two points {point1} and {point2}")
#         new_x = point1.x + point2.x
#         new_y = point1.y + point2.y
#         # print(f"{new_x}, {new_y}")
#         resultant_point = Point(new_x, new_y)
#         return resultant_point

#     def __mul__(self, scale):
#         new_x = self.x * scale
#         new_y = self.y * scale
#         return Point(new_x, new_y)

#     def __sub__(point1, point2):
#         new_x = (point1.x - point2.x) ** 2
#         new_y = (point1.y - point2.y) ** 2
#         distance = (new_x + new_y) ** 0.5
#         return round(distance, 2)

#     def __del__(self):  # destructor
#         print(f"{self} is being deleted")


# p1 = Point(1, 1)
# p2 = Point(5, 5)

# # print(p2)
# # print(p1 + p2)
# # print(p1 * 3)
# print(p1 - p2)


# result = eval(input("Enter an expression: "))
# print(result)
# print(type(result))
# "ram".upper()

# print([12, 3] * 3)
# print("ram" * 3)
