#.find() method is used to return the index at which the substring is located first
message="human"
print(message.find('h'))
#searches a in between 2nd and 5th index, not found so returns -1
print(message.find("h",2,5))

#TASK 1: Find position of first "a"
inp = input("Enter a string: ")
print(inp.find("a"))

# #TASK 2: Masking email address
email = input("Enter an email address: ")
symbol = email.find("@")
username = email[:symbol]
domain = email[symbol:]
maskedmail = username[0] + "*" * (len(username) - 2) + username[-1] + domain
print("Masked email:", maskedmail)

#.index() method locates the position of a string or substring
print(message.index("man"))
#print(message.index("hello")) gives error unlike in find where it returns -1 for 
# unmatched string or substring
print(message.index("man",0,11)) #returns the index at which the substring is located if it lies between 0 and 11

#strip, rstrip and lsstrip removes spaces from all sides, right side and left side respentively
text="           hi i am a robot      "
print(text.strip())
print(f"{text.rstrip()}hello")
print(f"{text.lstrip()}hello")

#.replace() method replaces the old value with new one
text1="i am a girl yes yes"
result=text1.replace("girl","person")
print(result)

#we can add a extra parameter to define how many occurence of the string or substring we want
#to remove
result1=text1.replace("yes","haha",1) #replaces one occurence of yes with haha
print(result1)

#.split() method divides te string values into different other values based on set
#parameter and returns as a list
text2="hi, how are you, all god, or not"
result2=text2.split(",")
print(result2)

#we can also specify the number of list values we want it to return by setting a parameter
result2=text2.split(",", 2)
print(result2)