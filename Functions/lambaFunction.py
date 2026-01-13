#lambda function is a small anonymous function
#it allows you to perform simple operations and take any number of arguments without defining a function
#way of creating one liner function

#syntax: lambda args:expression

sum= lambda x,y:x+y
print(f"sum is {sum(1,2)}")

#calculating square number
square= lambda x:x**2
x=int(input("enter a number:"))
print(f"square of {x} is {square(x)}")

#checking negative or positive
check= lambda x: 'positive' if x>0  else ('negative' if x<0 else 'zero')
print(check(0))

#lambda can be passed as an argument to higher order functions like map(), filter() and reduce()
#------map()---------
#maps all values to the arguments in lambda
values=[-1,0,5,9999999,1.5]
check= list(map(lambda x: 'positive' if x>0  else ('negative' if x<0 else 'zero'), values))
print(f"result for {values}:{check}")
print(f"result for {values}:{list(check)}") #we can do this too to print the list
#here we need not use check(values) because map method maps the arguments 

#----------filter()---------
#filters or removes the specified arguments
values=[1,2,3,4,8]
evenNumbers=filter(lambda x:(x%2==0),values)
print(f"the even numbers in list {values} are: {list(evenNumbers)}")

#-------reduce()----------
#it is applied to all the items in an iterable to reduce the result to a single value
#using for summing, subtracting, maximizing etc
from functools import reduce
values=[1,2,3,4,8]
max=reduce(lambda x,y:x if x>y else y, values)
print(f"the maximum value in {values} is: {max}")

values=[190,2,3,100]
difference=reduce(lambda x,y:x-y, values)
print(f"after subtracting {values} sequentially : {difference}")