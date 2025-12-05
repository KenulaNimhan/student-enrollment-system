class Student:

    # define constructor
    def __init__(self, name, age, email, password):
        self.studentId = ""
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def __str__(self) -> str:
        return f'Student Details\nname: {self.name}\nage: {self.age}'