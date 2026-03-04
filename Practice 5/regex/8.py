import re
# Split a string at uppercase letters
#(?=[A-Z]) splits before each capital letter
text = "HelloWorldPython"
result = re.split(r"(?=[A-Z])", text)
print(result)