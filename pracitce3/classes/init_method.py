"""
Using __init__ constructor
"""

class Person:
    def __init__(self, name, age):
        """Initializes name and age."""
        self.name = name
        self.age = age

person = Person("Ali", 20)
print(person.name, person.age)
