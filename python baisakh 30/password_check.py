password = input("Enter password: ")

at_least_1_number_exists = not password.isalpha()

if at_least_1_number_exists:
    print("Strong Password")
else:
    print("Weak Password")
