fruits=['Apple', 'strawberry', 'avocado', 'berries', 'pineapple']

#---adding items---
#.append() adds an item to the end of the list
fruits.append('guava')
print(fruits)

#.insert() adds the utem to the specified index
fruits.insert(2,'guava')
print(fruits) #since duplicate items can be added in a list there are two guavas 

#adding the items of a new list to an existing list
citrusFruits=['lemon','orange']
fruits.extend(citrusFruits)
print(fruits)
print(citrusFruits)

#---removing items----
#.remove() removes the first occurence of specified value
fruits.remove('guava')
print(fruits)

#.pop() removes and returns the last element by default, or the element at the given index.
result=fruits.pop(1)
print(fruits)
print(result)
print(len(fruits))
print(fruits[1])

#we can use a list constructor to build a list too
season=list(('Summer', 'winter'))
print(season)

#.clear() method removes the item from a list but doesnot delete list completely
citrusFruits.clear()
print(citrusFruits)

#del keyword removes the items at specified index or the list itself when index is not defined
del fruits[0]
print(fruits)

del fruits
# print(fruits) #retuns nameerror

#----sort method----
#sort() method sorts the list items in alphabetical/ascending order
fruit=['apple', 'avocado', 'berries', 'pineapple', 'guava', 'lemon', 'orange']
print(f'unsorted:{fruit}')
fruit.sort()
print(f'sorted:{fruit}')
fruit.sort(reverse=True)
print(f'reversely sorted:{fruit}')

a =['a',10,2j,True]
# a.sort()
# print(a)
# sorting is not supported for list having mixed datatypes

#---copy method---

seasonalFruits=fruit
print(seasonalFruits)
#copies exactly the items of fruit in seasonalFruits so when we changeany one list both the list changes
fruit.pop()
print(fruit,seasonalFruits)
seasonalFruits.pop()
print(fruit,seasonalFruits)

#HENCE we use .copy() method which simply copies the original list to newly formed list 
# without making eachother interdependent like when we used assignment opertaor previously

seasonalFruits=fruit.copy()
fruit.pop()
print(fruit,seasonalFruits)
seasonalFruits.pop()
print(fruit,seasonalFruits)

#----reverse method-----
#.reverse() method simply reverses a list
print(f'unreversed:{fruit}')
fruit.reverse()
print(f'reversed:{fruit}')

#-----count method----
#counts the number of times any values is rpeeated in the list
repeated=['lemon','prange','lemon']
fruit.extend(repeated)
result=fruit.count('lemon')
print(fruit)
print(f'the number pf times lemon is repeated : {result}')

#------index method---
#it returns  index values is the list item
print(f'the index value of lemon is {fruit.index("lemon")}')

#---------opertaors in list-----------
#arithmetic operator
colorfulFruits=['dragon fruit','strawberry']
seasonalFruits=['grapes','mangoes']
citrusFruits=['lemon','orange']
allFruit=colorfulFruits + seasonalFruits + citrusFruits
print(allFruit)
#using + operator can let you merge multiple lists to an existing list
print(f"unextended:{citrusFruits}")
colorfulFruits.extend(citrusFruits+seasonalFruits)
print(f"extended:{colorfulFruits}")

#membership operator
#checks if an item is inside a list
print(f'lemon falls in citrus fruits : {"lemon" in citrusFruits}')
print(f'grapes falls in citrus fruits : {"grapes" in citrusFruits}')
print(f'orange donot fall in citrus fruits : {"orange" not in citrusFruits}')

#identity operator
#checks if two lists are same
seasonalFruits=colorfulFruits
print(f"seasonal fruit is colorful fruit : {seasonalFruits is colorfulFruits}")

seasonalFruits = colorfulFruits.copy()
print(f"seasonal fruit is colorful fruit : {seasonalFruits is colorfulFruits}")