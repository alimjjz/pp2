import re
# Match a string with a followed by 2 to 3 b
#b{2,3} means the letter b appears from 2 to 3 times
text = input()
if re.fullmatch(r"ab{2,3}", text):
    print("Match")