"""
Function arguments examples: positional and default arguments
"""

def greet_user(name, greeting="Hello"):
    """Greets a user with a custom or default greeting."""
    print(f"{greeting}, {name}!")

greet_user("Ali")
greet_user("Dana", "Good morning")
