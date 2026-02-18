"""
Using lambda with sorted()
"""

students = [
    {"name": "Ali", "grade": 85},
    {"name": "Dana", "grade": 92},
    {"name": "Timur", "grade": 78}
]

sorted_students = sorted(students, key=lambda student: student["grade"])
print("Sorted students:", sorted_students)
