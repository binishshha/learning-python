message = "i AM a huMAN "

s = "Der Fluß"

#first letter capital aru small
print(f"capitalized:{message.capitalize()}")
#sabai letter capital
print(f"upper:{message.upper()}")
#sabai letter small and same as lower but is used when the input is expected in multiple languages ani more agressive
#unicode aware becz supports multiple languge
print(f"casefold:\nfirst:{message.casefold()}\nSecond:{s.casefold()}")
#works wit english and ascii character better
print(f"lower:\nfirst:{message.lower()}\nSecond:{s.lower()}")
#1st letter of every word capital
print(f"title:{message.title()}")
print("don't go".title()) #OUTPUT: Don'T Go (incorrect gramatically)