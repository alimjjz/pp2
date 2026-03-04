import re
# Match a string that starts with a and ends with b
# a.*b means a, then any characters ending with b
text = "aasdb"
if re.fullmatch(r"a.*b", text):
    print("Match")