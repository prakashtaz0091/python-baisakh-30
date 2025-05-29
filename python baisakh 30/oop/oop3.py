class User:
    def __init__(self, name, email, phone, password):  # constructor
        self.name = name
        self.email = email
        self.__phone = ""

        self.phone = phone  # using setter to avoid invalid phone number assignment

        self.__password = password

    @property
    def phone(self):
        first_two_numbers = self.__phone[:2]  # slicing string
        last_three_numbers = self.__phone[
            -3:
        ]  # slicing string but using negative index
        return f"{first_two_numbers}******{last_three_numbers}"  # actual_ph_no=> 9800000000 => 9800*****00

    @phone.setter
    def phone(self, new_phone):
        if len(new_phone) != 10:
            raise ValueError("Phone number must be 10 digits")

        try:
            int(new_phone)
        except Exception:
            raise ValueError("Phone number must be a number")

        if new_phone[:2] not in ("98", "97"):
            raise ValueError("Phone number must start with 98 or 97")

        self.__phone = new_phone

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        pass
        # if len(new_password) < 8:
        #     raise ValueError("Password must be at least 8 characters long")
        # self.__password = new_password

        # add additional validation as HW


# ram = User("ram", "ram@ram", "980000000a", "ram1234")
# print(ram.phone)
# ram.phone = "980000000a"
# print(ram.phone)


class Student(User):  # Inheriting User class to get all the properties and methods
    # here User is called as superclass (parent class)
    # Student class is called as subclass (child class)
    # User class -> __init__
    def __init__(
        self,
        name,
        email,
        phone,
        password,
        class_,
        section,
        roll_no,
    ):
        super().__init__(name, email, phone, password)  #   User.__init__
        self.class_ = class_
        self.section = section
        self.roll_no = roll_no

    def show_info(self):
        info = f"""
        Name: {self.name}
        Email: {self.email}
        Phone: {self.phone}
        Class: {self.class_}
        Section: {self.section}
        Roll No: {self.roll_no}
        """
        print(info)


# ram = Student("ram", "ram@ram", "9800000001", "ram1234", "10th", "A", "1")
# # print(ram.phone)
# # ram.phone = "980000000a"
# # print(ram.phone)
# ram.show_info()


class Staff(User):
    def __init__(self, name, email, phone, password, salary):
        super().__init__(name, email, phone, password)
        self.salary = salary

    def show_info(self):
        info = f"""
        Name: {self.name}
        Email: {self.email}
        Phone: {self.phone}
        Salary: {self.salary}
        """
        print(info)


# hari = Staff("hari", "hari@hari", "9800000002", "hari1234", 50000)
# hari.show_info()


class Teacher(Staff):
    def __init__(self, name, email, phone, password, salary, subjects):
        super().__init__(name, email, phone, password, salary)
        self.subjects = subjects

    def show_info(self):
        info = f"""
        Name: {self.name}
        Email: {self.email}
        Phone: {self.phone}
        Salary: {self.salary}
        Subjects: {" | ".join(self.subjects)}
        """
        print(info)


shyam = Teacher(
    "shyam",
    "shyam@shyam",
    "9800000003",
    "shyam1234",
    60000,
    ["English", "Nepali", "Maths", "Science"],
)
# shyam.show_info()


# class A:
#     pass


# class B:
#     pass


# class C(A, B):
#     pass


# c1 = C()
# c1.show_info()
# print(C.__mro__)
