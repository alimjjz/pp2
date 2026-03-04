import re
# Replace space, comma, or dot with ':'
# [ ,.] matches space, comma, or dot, re.sub - find and replace
text = "Hello, world. Python"
result = re.sub(r"[ ,.]", ":", text)
print(result)