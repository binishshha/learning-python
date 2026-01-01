name="hari"
age=22
print(name + " is" + str(age) + " years old") #not suitable for proper concatenation
#so we use f string 
print(f"{name} is {age} years old")
#if you want to show age in double quoatation
print(f"{name} is \"{age}\" years old")
#cn use escape characters like \n \h \r \b too
print(f"name:{name} \nage:{age} years old")