#sets are immutable, unordered and non-duplicable collection of elements
#elemebts can be added or removed either unlike in tuples

x={'ram',11,False,0,2.999}
print(x)
#output : {False, 2.999, 11, 'ram'}
#the order of output is diff from the way we inputted
#since order doesnot mattter her, we cannot access the elements using index method
#only the first occurance of the duplicate element if printed/stored
#here 0 is not printed because of its property of uniqueness
#since 0 and False gives the same intent they are not printed twice and the first occurence of it i.e. Fale is printed

print(len(x))

#can use operators too
#eg: membership operator
print(f"ram is in the set : {'ram' in x}")
#eg: identity operator
print(f"False is 0: {(False is 0)}")
#arithmetic operator is not supported

#---adding items------
#----.add() method---
#allows you to add a value to an existing set
fruit={'apple','banana'}
fruit.add('kiwi')
print(f'added: {fruit}')

#------.update() method---
#allows you to add the values of an existing set to another existing set(nayai banauda ni huncha)
citrusFruits={'lemon','orange'}
fruit.update(citrusFruits)
print(f'updated: {fruit}')

#we can use an operator too
citrusFruits |= fruit

#---------removing items-------
#-----remove() method------------
print(f"original:{fruit}")
fruit.remove('apple')
print(f"after removal:{fruit}")
# fruit.remove(1) #cannot be removes again keyerror

#----discard method-----
#it is used if you dont want the keyerror
fruit.discard('apple')
print(f"after discard: {fruit}")

#------pop method----
#returns the popped value
#cannot determine what value might be popped
fruit.pop()
print(f"after popping :{fruit}")

#clear() method empties the set
fruit.clear()
print(f"cleared : {fruit}")

#del deletes the varaible fruit
del fruit