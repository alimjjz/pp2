import re
text = input()
if re.fullmatch(r"ab*", text): #r-raw string,it checks if the string text matches the pattern ab*.
                                #string must start with a and zero or more b characters.
                                #re.fullmatch() ensures that the whole string fits the pattern.
    print("Match")
else:
    print("No match")