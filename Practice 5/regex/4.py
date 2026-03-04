import re
# Find words starting with a capital letter followed by lowercase letters
# [A-Z][a-z]+ matches a capital letter and then lowercase letters
text = "Hello World Python"
result = re.findall(r"[A-Z][a-z]+", text)
print(result)