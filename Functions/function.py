#a function is a block of code that runs on a function call
#may contain  parameters
#can return data as a result

#function definition without parameters
def hello():
    print("hello world!!")

#syntax to call a function: function_name(agr1, arg2, ...)
hello()

#function definition without parameters
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

#--------------default values-----------
#we add default values to the parameters so that when the function call doesnot pass enough args we can use default parameter values and avoid error
def sum(a:int=0, b:int=0): #a default parameter never follows a non default parameter so the optional parameter should always be the last one
    summ=a+b
    return summ
print(sum()) #we cannot pass an empty function call if parameters are defined
print(sum(2))



