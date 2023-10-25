class Student:
    school = "DIO" # Class attribute

    def __init__(self, name, registration):
        self.name = name # Instance attribute
        self.registration = registration # Instance attribute

    def __str__(self) -> str:
        return f"{self.name} - {self.registration} - {self.school}"


def display_values(*objs):
    for obj in objs:
        print(obj)


student_1 = Student("Guilherme", 1)
student_2 = Student("Giovanna", 2)
display_values(student_1, student_2)

Student.school = "Python"
student_3 = Student("Chappie", 3)
display_values(student_1, student_2, student_3)