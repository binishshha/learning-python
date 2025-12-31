#variables should start be alphanumeric characters and start with an alphabet or underscore
#variables are case sensitive
#shouldnot start with special characters like # $ % ^
#value for variables is literal

firstname='hari'
#print(FirstName) is wrong
print(firstname)

#set variable in 2 ways
x=5
y=str(5) #typecasting
print(type(x))
print(type(y))

#types of datatypes

#numeric: int, float, complex
a=10 #int
print(a)
x=10.0020 #float
print(x)
b=2j #complex
c=4j+1
print(b,c)

#boolean: bool
isLive= True
print(type(isLive))

#sequence: list, tuple, range
#mapping: dict
#set: set, frozenset
#none: None

#defining variables and literals at the same time
a=b=c=0
print(a,b,c)
a, b, c= 1, 2, 3
print(a,b,c)

#print("value of a is:"+a) is wrong
# we can only concatenate two strings together
#SO
print("the value of a is:"+str(a))