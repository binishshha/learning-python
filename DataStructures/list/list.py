#list is a built-in, ordered/indexed and changeable/mutable collection on items that allows duplicate members and can contain any datatype
a=['x', '2.11111', 1.2, 2j+1]
print(a)

fruits=['Apple', 'Banana', 'Apple', 'Kiwi']
print(fruits)
#print the kength of a list using len(); the index of list runs from 0 to n 
#we can also index the list backwards from the last element in the list to first i.e. last element is -1, then -2, -3...
print(len(fruits))

#---accessing items---
print(fruits[:-1]) #returns all value from the start upto -2
print(fruits[1::3]) 
print(fruits[::-1]) #reverses a list
print(fruits[::-2]) #reverses a list and returns the value with gap=-2

#changing the items 
fruits[1:3]=['mango']
print(fruits) #new list
print(len(fruits)) #indexing changes too

#we can increase the list items too
fruits[1:3]=['strawberry','avocado','berries','pineapple']
print(fruits)
print(len(fruits))

