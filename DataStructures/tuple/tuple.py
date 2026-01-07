#tuples are ordered, duplicable but immutable built-in data sructures i.e elements cannot be modified
#elments cannot be added or removed in it
gradeTuple= ('C','D','A','A','B','B','A', 100)
print(gradeTuple)
# gradeTuple[1]=10000 cannot be modified

# To change tuple data, create a list copy using list(), modify the list, and convert it back if needed
gradeList=list(gradeTuple)
print(f"unmodified tuple:{gradeTuple}")
gradeList[1]=10000
print(f"modified into list:{gradeList}")
gradeTuple=tuple(gradeList)
print(gradeList)
print(gradeTuple)
gradeList[0]=99 #still a list
print(gradeList)
#then you can use any list methods to modify it

#-----tuple methods-----

#-------count method----------
#.count() is used to count the repetituion of elements inside a tuple
count=gradeTuple.count('A')
print(count)

#-------index method---------
#returns the index value at which the tuple element is first located
print(f"A is at index : {gradeTuple.index('A')}")

#-----------operators in tuple-----
roll=(10,20,30)
names=('ram','sita','hari')

studentInfo=roll+names
print(studentInfo)

studentInfo2=roll*2 #stires the elements in tupke twice
print(studentInfo2)

#membership operators like in, not in 
#identity operator like is 
#both can be used too; same like in lists