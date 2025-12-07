import re

# define validator constants
EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

class Student:

    # define constructor
    def __init__(self, name, age=None, email=None, password=None, studentId=None):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    # setters with validators
    def set_studentId(self, id):
        self.studentId = id

    def set_age(self, age):
        if (age>=18 and age<=40):
            self.age = age
        else:
            raise ValueError("Age is invalid")

    def set_email(self, email):
        if (re.match(EMAIL_REGEX,email)):
            self.email = email
        else:
            raise ValueError("Email is invalid")

    def set_password(self, password):
        if (len(password)>5):
            self.password = password
        else:
            raise ValueError("Password is invalid")

    def __str__(self) -> str:
        return f'Student Details\nname: {self.name}\nage: {self.age}'