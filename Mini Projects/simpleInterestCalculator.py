def simpleInterest(principal,rate,time):
    interest=(principal*rate*time)/100
    return interest

p=float(input("Enter the principal amount:")) #we must typecast the input type; by default stores as string
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time in years:"))
result=simpleInterest(p,r,t)
print(f"""the simpleinterest calulated for:\nprincipal amount:{p}\nrate of interest:{r}\ntime(in years):{t}
      Hence, simple interest is:{result}""") #used triple quote to allow line breaking