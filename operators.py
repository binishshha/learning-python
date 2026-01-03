#arithmetic operators: + - * / %
#performa mathematical operations on operands
a=5; b=6
sum= a+b; diff=a-b; mul=a*b; div=a/b; floorDiv=a//b; mod=a%b; exp=a**b; #exp is power
print(f"{a}+{b}={sum}")
print(f"{a}-{b}={diff}")
print(f"{a}*{b}={mul}")
print(f"{a}/{b}={div}")
print(f"{a}//{b}={floorDiv}")
print(f"{a}**{b}={exp}")

#assignment operators: += -+ *
#takes operand on the righ side performes an operation on the operand on the righht side of the operator
a=5; b=6
a+=b
print(a,b)
#a is assigned a new value by adding b

#comparison operators: > < >= <= !=
#compares two operands
a=10; b=5
print(a>=b)#TRUE
print(a!=b)#TRUE
print(a<b)#FALSE

#logical: and or not 
x=10; y=20
result=(x<y and y>x) 
print(result)#returs boolean value as result
print(not(result))#works on bool datatype and returns False as the vallue of result is True from prev line
print(not(a==b)) #True

#OTHER OPERATORS
#bitwise: & >> << | ^
#identity: is , is not
#membership: in, in not

#operator precedence plays a uge role in how the output is going to be interpreted