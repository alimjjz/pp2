"""
Class vs instance variables
"""

class Student:
    school_name = "High School"

    def __init__(self, name):
        self.name = name

student = Student("Dana")
print(student.name)
print(Student.school_name)
