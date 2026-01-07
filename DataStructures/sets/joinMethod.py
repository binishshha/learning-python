#---------UNION------
class1={'ram','sam','hari'}
class2={'sita','gita','hari'}

#union() method allows you to combine two existing set and set it to a new set
#without assigning it to a new variable no independent sets are updated
#the update()method only updates an existing set but cannot create a new one
classes = class1.union(class2)
print(f"class1={class1}")
print(f"class2:{class2}")
print(f"union: {classes}")

#we can also use | operator inplace of union method
classesop=class1 | class2
print(f"classes using operator: {classesop}")
print(f"class1={class1}")
print(f"class2:{class2}")

#---------INTERSECTION-------------
commonName=class1.intersection(class2)
print(f"common name: {commonName}")
print(f"class1={class1}")
print(f"class2:{class2}")
#use & operator
commonName1= class1 & class2
print(f"using operator:{commonName1}")

#this updates the class 1 with common names onle and removes other names
class1.intersection_update(class2)
print(f"class1={class1}")
print(f"class2:{class2}")
#use &= operator
class1 &= class2
print(f"class1={class1}")
print(f"class2:{class2}")