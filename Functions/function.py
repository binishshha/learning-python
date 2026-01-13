#a function is a block of code that runs on a function call
#may contain  parameters
#can return data as a result

#function definition without parameters
def hello():
    print("hello world!!")

#syntax to call a function: function_name(agr1, arg2, ...)
hello()

#function definition with parameters
#parameters are variable listed inside function definition
def sum(a:int, b:int): 
    #we can or cannot specify the data type for each parameter by using a colon : after each parameter
    #they are called type hints
    #typehints are ignored during runtime because ut doesnot enforce a data type but guves a hint on what value is expected
    summ=a+b
    return summ
#function call with arguments
#arguments are values passed to function when it is called
print(sum(1,2))
print(sum([1,2,3],[2,3,4])) #cocncatenates a list
# print(sum(1,'a')) #gives you type error because python cannot add a integer and string]
# print(sum()) #we cannot pass an empty function call if parameters are defined

#--------------default or optional parameter values-----------
#lets you call a function even if all args are nit provided
#we add default values to the parameters so that when the function call doesnot pass enough args we can use default parameter values and avoid error
def sum(a:int=0, b:int=0): #a default parameter never follows a non default parameter so the optional parameter should always be the last one
    summ=a+b
    return summ
print(sum()) #we cannot pass an empty function call if parameters are defined and default parameter values are not set
print(sum(2))

# if you dont define parameter type then we can just add default values as def sum(a=0,b=1)


#------------ARGUMENTS-------------

#---------positional arguments---------
#defined in order of the parameters placed
sum(1,2) #where 1 is for number1 and 2 is for number2

#---------------keyword arguments(kwargs)------
#defining keywrod args in function call lets you define the value of variables in a call itself
#it allows passing values to a function by explicitly naming the parameter
#the order of defining the arguments should not comuplsorily match the order of defining parameters
print(sum(b=10))
print(sum(a=1,b=10))

#--------------arbitary positional arguments-----------
#they are used when the number of positional arguments you want to define is not fixed
#stores value as a tuple
def colors(*args):
    for items in args:
        print(items.upper()) #its a tuple
        
colors("red","blue")
colors("red","blue","yellow") #you can pass any datatype int, float etc together
colors()

#--------arbitary keyword arguments---------
#allows you to add any number of keyword arguments
#stires each key=value pair i.e. arguments in dictonary
def colors(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        
colors(name="blue",shade1="yellow",shade2="green")
colors()

#-----USE
#functiuon allows you to write reusable block of code which improves codes' maintainability
#holds encapsulation property as it is defined with scope