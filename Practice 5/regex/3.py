import re
# find lowercase words connected with underscore
# [a-z]+_[a-z]+ matches lowercase letters joined with '_'
text = input()
result = re.findall(r"[a-z]+_[a-z]+", text)
print(result)