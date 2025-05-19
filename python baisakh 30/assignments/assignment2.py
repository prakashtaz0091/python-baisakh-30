# # Python Assignment with Solutions
# # Covers: Variables, Data Types, Operators, Input/Output, Formatted Strings, Conditional Statements

# # 1. Voting Eligibility
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# # 2. Odd or Even Checker
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# # 3. Positive, Negative, or Zero
# n = float(input("Enter a number: "))
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")

# # 4. Temperature Feedback
# temp = float(input("Enter temperature in Celsius: "))
# if temp >= 30:
#     print("It's hot today.")
# elif temp >= 15:
#     print("Nice weather!")
# else:
#     print("It's cold today.")

# # 5. Simple Calculator
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")
# if op == "+":
#     print(f"Result: {a + b}")
# elif op == "-":
#     print(f"Result: {a - b}")
# elif op == "*":
#     print(f"Result: {a * b}")
# elif op == "/":
#     if b != 0:
#         print(f"Result: {a / b}")
#     else:
#         print("Division by zero error")
# else:
#     print("Invalid operator")

# # 6. Area Type Checker
# area = float(input("Enter area in sq units: "))
# if area < 100:
#     print("Small Area")
# elif area <= 500:
#     print("Medium Area")
# else:
#     print("Large Area")

# # 7. BMI Calculator
# weight = float(input("Enter weight in kg: "))
# height = float(input("Enter height in meters: "))
# bmi = weight / (height**2)
# print(f"Your BMI is {bmi:.2f}")
# if bmi < 18.5:
#     print("Underweight")
# elif bmi < 25:
#     print("Normal")
# elif bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")

# # 8. Student Grade Calculator
# marks = int(input("Enter marks out of 100: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# # 9. Triangle Type Checker
# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c: "))
# if a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

# # 10. Volume Checker
# side = float(input("Enter side of cube: "))
# volume = side**3
# print(f"Volume: {volume}")
# if volume > 1000:
#     print("Large cube")
# else:
#     print("Small cube")

# # 11. Password Checker
# password = input("Enter password: ")
# if password == "admin123":
#     print("Access Granted")
# else:
#     print("Access Denied")

# # 12. Bus Fare Calculator
# age = int(input("Enter your age: "))
# if age < 5:
#     print("Fare: Free")
# elif age <= 18:
#     print("Fare: ₹10")
# elif age <= 60:
#     print("Fare: ₹20")
# else:
#     print("Fare: ₹5")

# # 13. Water Level Checker
# water = int(input("Enter water level in liters: "))
# if water < 100:
#     print("Please refill water.")
# elif water <= 1000:
#     print("Water level is sufficient.")
# else:
#     print("Overflow warning!")

# 14. Electricity Bill Estimator
# units = int(input("Enter electricity units used: "))
# bill = 0
# if units <= 100 and units > 0:
#     bill = units * 5
# elif units <= 300:
#     price_100_units = 100 * 5
#     remaining_units = units - 100
#     price_remaining_units = remaining_units * 7
#     bill = price_100_units + price_remaining_units
# else:
#     bill = 100 * 5
#     remaining_units = units - 100
#     bill = bill + 200 * 7
#     remaining_units -= 200
#     bill = bill + remaining_units * 10


# print(f"Your bill is ₹{bill}")


# 14 Electricity Bill Estimator
# reading = int(input("Enter your units consumed::"))
# if reading > 0 and reading <= 100:
#     total = reading * 5
# elif reading <= 300:
#     total = (reading - 100) * 7 + 100 * 5
# else:
#     total = (reading - 300) * 10 + 200 * 7 + 100 * 5
# print("Your Bill ::", total)

# # 15. Leap Year Checker
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# # 16. Vowel Checker
# ch = input("Enter a letter: ")
# if ch.lower() in "aeiou":
#     print("It is a vowel.")
# else:
#     print("It is not a vowel.")

# # 17. Email Validator
# email = input("Enter your email: ")
# if "@" in email and (email.endswith(".com") or email.endswith(".org")):
#     print("Valid Email")
# else:
#     print("Invalid Email")

# # 18. Name Greeting with Length Check
# name = input("Enter your name: ")
# if len(name) < 3:
#     print("Name too short!")
# else:
#     print(f"Hello {name}, nice to meet you!")

# # 19. Username Availability
# username = input("Enter desired username: ")
# if username in ["admin", "user", "test"]:
#     print("Username not available")
# else:
#     print("Username available")

# # 20. Fuel Level Warning
# fuel = float(input("Enter fuel level in liters: "))
# if fuel < 5:
#     print("Refuel now!")
# elif fuel <= 20:
#     print("Fuel is low")
# else:
#     print("You're good to go")
