import math

print(math.pi)
print(math.e)
print(math.inf)
print(math.tau)
print(math.pow(2,3))
print(math.sqrt(144))
print(math.nan)

print(math.factorial(5))
print(math.fabs(-100)) #always returns float value
print(math.gcd(2,4,8))

print(math.floor(4.2))
print(math.floor(4.7)) #nearest lower value
print(math.ceil(4.2)) #nearest higher value

print(round(5.5))
print(round(5.1))

#-----area of a circle-------
def area(radius):
    return math.pi*math.pow(radius,2)

result=area(7)
print(f"area of a circle: {result}")