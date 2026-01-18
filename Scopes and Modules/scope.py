# scope of a variable refers to the part of the program where the variable is ccessible

#different scope of a variable are local, global, enclosing and built-in

#locl scope refers to variables defined withina function or method
#they are only accessible within the function they are defined in

#enclosing scope refers to the variables that are defined in the outer function and can be accessed by the inner functions
# i.e. it is used to define the scope for nested functions

# global scope refers to the variables that can be accessed from anywhere in the program
# they are the top module of the program above any claa or function

#built in scope refers to names/methods like print and len that the python always knows, no matter where youa re in the program

# whenever you reference a variable in a function, it first checks locally
# then checks any enclosing functions, then globally 
# and finally checks if it is any built in variable

#---EXAMPLE---
a=90  #global variable, can be accessed from anywhere
def outer_function():
    b=40 #enclosing, can be accessed by inner_function() too
    def inner_function():
        c=60 #local, can be accessed inside inner_function() only
        print(a,b,c)
    # return inner_function #esto garda closure huncha i.e. callable function
    inner_function()

outer_function()
# print(a,b,c) #b and c cannot be accessed
# i=outer_function()
# i()

#------global keyword-------
# in order to modify a global variable, we must use keyword global
a=99
def modify():
    global a #making a variable global
    a=20

print(f"before modification: {a}")
modify()
print(f"before modification: {a}")

#------nonlocal keyword----
a=1  #global 
def outer_function():
    a=11 #enclosing
    def inner_function():
        nonlocal a #makes a=111 nonlocal
        a=111 
    inner_function()
    print(a) # even after calling innerfuntion alr , we still have the value for a=11
    # beacause a=111 is a local variable for inner_function() 
    # so we use nonlocal keyword and make a=111 a nonlocal variable

outer_function()
print(a) #because a is a global vraible so it prints global a's value i.e. 1