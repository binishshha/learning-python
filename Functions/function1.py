#-------------PARAMETERS-----------
#they are used to assign values to a function
#defined in function definiton

#----------Positional parameters----------
#arguments must be passed in exact order they are defined in function defn
##assigns value based on their position

def student(name, marks):
    print(f"{name} scored {marks}")

student("ram",90)
student(90,"ram") #name is assigned 90 and marks is assgined ram solely on the position of arguments called inside a function

#---------Keyword parameter--------
# arguments can be passed by explicitly naming the parameter in a function call itslef
#the order of parameters doesnot matter
#can be used with optional parameters too
student(marks=90,name="ram")

#note: keyword parameters should always come after positional parameters

#--------variable-length/arbitary positional parameters-----
# uses *args in func def to college extra positional arguments in a tuple
# can hold any number of arguments 

#--------variable-length/arbitary keyword parameters-----
# uses **kwargs in func def to college extra keyword arguments in a dictionary
# can hold any number of arguments 

#--------mixed parameters-----
#here you can pass both arbitary arguments and keyword arbitary arguments
#the order for defining such a parameter should always be *args , **kwargs
#cannot place positional argu,ments after keyword arguments

def colors(*args,**kwargs):
    for items in args:
        print(items.upper()) #its a tuple

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print("---------1st----------")
colors("red","blue",name="blue",shade1="yellow",shade2="green")
print("---------2nd--------")
# colors(name="blue",shade1="yellow",shade2="green","red","blue",1100) #syntax error
colors(name="blue",shade1="yellow",shade2="green")
print("---------3rd---------")
colors("red","blue")
colors()

#---------positional only parameters----------
#whenever / is placed after a parameter, it specifies that all arguments before it must be passed as positional 
def posOnly(a,y,/,z,b):
    print(f"a:{a}")
    print(f"y:{y}")
    print(f"z:{z}")
    print(f"b:{b}")

posOnly(1,2,3,4)
posOnly(1,2,b="ram",z=3)
# posOnly(y=2,a=1,b=4,z=3) #syntax error

#-------------keyword only parameters--------
#whenever * is defined before a parameter, it specifies that all arguments after it must be keyword arguments
def keywOnly(a,y,*,z,b):
    print(f"a:{a}")
    print(f"y:{y}")
    print(f"z:{z}")
    print(f"b:{b}")

keywOnly(1,2,z=4,b=3)
keywOnly(y=2,a=1,b=4,z=3)
# keywOnly(y=2,a=1,4,3) #syntaxerror

#-------------mix-only parameters----------
#you can only define keyword onlyparameters after positional only parameters
def mixOnly(a,y,/,*,z,b):
# def keywOnly(a,y,*,/,z,b): #WRONG
    print(f"a:{a}")
    print(f"y:{y}")
    print(f"z:{z}")
    print(f"b:{b}")

mixOnly(1,2,z=4,b=3)
# mixOnly(z=4,b=3,1,2)
# mixOnly(1,2,3,4)

#--------return value---------
# in a function you can return a value back to the calling function by using return keyword
def sum(a, b): 
    result=a+b
    return result
    return None #this line wont execute because a function has retuned a value already

result=sum(1,2)
print(result)

#-----pass-----
#it allows you to execute an empty function without writing a block of code in it without causing error
def add(a,b):
    pass