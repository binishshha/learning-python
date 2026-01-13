#recursion is a powerful technique in which a function calls itself again and again until some condition is met
#it lets you manage long tedious blocks of code amd simplifies a problem
#ideal for divide and conquer problems

#factorial of a number

#regular way of solving a factorial problem
def factorial(number):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact

#recursively solving a factorial problem
def recursiveFact(n):
    fact=1
    if n==1: #base condition
        return fact 
    else:
        return n*recursiveFact(n-1) #recursive block

n=int(input("Enter a number:"))
result=factorial(n)
print(f"the factorial for {n} is: {result}")
result=recursiveFact(n)
print(f"the factorial for {n} is: {result}")

#cons of recursion:
#difficulty debugging
#performence overhead
#memory intensive