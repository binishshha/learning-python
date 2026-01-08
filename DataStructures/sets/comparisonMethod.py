#comparison mehtod compares two sets; checks wheather the set is a subset or superset of any set 
#returns the oputput as True or False

class1 = {'ram', 'sam', 'hari'}
class2 = {'sita', 'gita', 'hari'}
class3={'binisha','sanisha','bipisha'}

#.isdisjoint() checks if two or more sets have null intersection and returns true if satisfied
print(f"class 1 is disjoint of class 2 and class 3: {class1.isdisjoint('class2+class3')}")
print(f"class 1 is disjoint of class 3: {class1.isdisjoint(class3)}")

#.issubset checks if any two set have intersecting values
print(f"class 1 is subset of class 2: {class1.issubset(class2)}")
print(f"class 1 is subset of class 3: {class1.issubset(class3)}")

#.issuperset() checks if the set lies within a set
class4 = {'sita', 'gita'}
print(f"class 4 is superset of class 2: {class2.issuperset(class4)}")
#all item in class2 lies in class4 and class4 is it's superset