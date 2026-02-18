"""
Instance methods example
"""

class Calculator:
    def add(self, a, b):
        """Returns sum of two numbers."""
        return a + b

calc = Calculator()
print("Sum:", calc.add(5, 7))
