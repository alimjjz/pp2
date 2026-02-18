"""
Multiple inheritance example
"""

class Father:
    def skill(self):
        print("Programming")

class Mother:
    def skill(self):
        print("Design")

class Child(Father, Mother):
    pass

child = Child()
child.skill()
