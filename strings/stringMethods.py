#.find() method is used to locate the letter at an exact index

#TASK 1: Find position of first "a"
inp = input("Enter a string: ")
print(inp.find("a"))

#TASK 2: Masking email address
email = input("Enter an email address: ")
symbol = email.find("@")
username = email[:symbol]
domain = email[symbol:]
maskedmail = username[0] + "*" * (len(username) - 2) + username[-1] + domain
print("Masked email:", maskedmail)