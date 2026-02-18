"""
Example of *args and **kwargs
"""

def show_args(*args):
    """Prints all positional arguments."""
    for value in args:
        print("Arg:", value)

def show_kwargs(**kwargs):
    """Prints all keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_args(1, 2, 3)
show_kwargs(name="Ali", age=20)
