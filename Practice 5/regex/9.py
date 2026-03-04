import re
# Insert spaces before capital letters
# add space before every uppercase letter
text = "HelloWorldPython"
result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)