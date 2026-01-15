#procedural programming involves invoking a function/method by passing vales
#oop creates object and organizes them in a class
#helps to keep code DRY(Dont Repeat Yourself)
#makes code easier modify, debug and maintain

#components: 1) object and 2) classes

#---object-----
# is an entity/thing
# models real world object, concept, process
# has a set of  properties/attributes or actions

#------class------
# is a logical entity
#group of objects with common properties
# they are the prototype or blueprit from which objects are created
# has a set of attributes that describes every object
# OR set of behaviour or actions that every object can perform (they are the functions or methods defined inside a class)

#----eg---for a class Car having attribute brand, color and behaviours start, stop, accelreate
#object car1 and car2 can be created 
#attributes for car 1: brand->tesla, color->pink
# behaviours for car1: start,stop, accelerate
#attributes for car 2: brand->ferrari, color->brige green
# behaviours for car2: start,stop, accelerate

#attributes and ebhaviours are class members

#------------Creating a class--------
# a class should be created by defining a class keyword and a class Name
# class name should always start with uppercase
class Car: #class is created
    #-----------------creating attributes------------
    #attributes in a class defined their property and are defined using variables
    brand= "Tesla" #attribute name is created with value tesla but we neednot specify values after creatig an object
    color="pink"
    #behaviours are defined as a function inside the class

#in procedural programming, when you define a function you must call it or else the block of code inside it wont excute
# similarly here in order to invoke a class we must create an object that would help us access the class members
car1=Car() #created an object car1 for class Car using class car 
car2=Car() #created an object car2 for class Car

print(f"car1's brand is:{car1.brand}") #using object car1 and syntax car1.attribute , we can access the members inside class
print(f"car2's brand is:{car2.brand}") #attributes are shared by all objects until overriden
# you can modify the value for object car2
car2.brand="ferrari"
print(f"car2's brand is:{car2.brand}")

#brand name not chnaged for object car1
print(f"car1's brand is:{car1.brand}")

#suppose
list1=[1,2,3,4,5,6]
list1.pop(1) #pop is a method from inbuilt class class List that is invoked using object list1


#-----Constructors------
#they are the special method that is automatically called when an object is created 
#in python __init__ method is used to define a constructor
# it doesnot return anything 
# it initializes objects attributes/states
# this method used self to denote current object

# syntax:
# def __init__(self, param1,...):
#     self.attribute1=value1
#     ....

#you must pass the parameter name while creating an object now
#self is a parameter that allows you to refer to the current instance of a class
#it keeps track of the sttributes of it's object and allows methods to access and mofify it
#self is not a kkeyword but it is just a parameter and you can use any name for eg. abc, xyz instead of self
class Carr:
    def __init__(self,brand,color):
        # self.brand is the attribute defined in object and brand is the value passed as parameter
        self.brand=brand
        self.color=color
        
    def displayInfo(self):
      print(f"the car's brand is {self.brand} and color is {self.color}")

    def __str__(self):
        return {self.brand}, {self.color} #DUNDER NETHOD

car1=Carr('tesla','pink')
car2=Carr('brand','beige green')
#accessing cars detail using attribute access method
print(f"Car 1 info: {car1.brand} {car1.color}") 
print(f"Car 2 info: {car2.brand} {car2.color}")

# accessing cars detail using funstion method
# use of self as  a parameter allows you to display info without passing any parameters;it uses car1 i.e. object ko values
car1.displayInfo()
car2.displayInfo()

#suppose if i want to modify the first object's color

car1.color="brown"
print("after changing first car's attribute values")
car1.displayInfo()
car2.displayInfo() #remains just the same

#---------------Dunder methods---------
# they are the special in-built underscore methods in python that specifies a specific behaviour

#eg: __init__ function acts as a default constructor for all classes 
# it is automatically called whenever a object is created
#it assigns vaalues to the sttributes of a class

#__str__ method
#automatically called when an object is converted to string using print or f-string
#using str allows us to easily access the class members by using object name and not functions or attribute method
class Carrr:
    def __init__(self,brand,color):
        # self.brand is the attribute defined in object and brand is the value passed as parameter
        self.brand=brand
        self.color=color

    def __str__(self):
        return f"{self.brand} and {self.color}" #DUNDER NETHOD

car1=Carrr('tesla','pink')
car2=Carrr('brand','beige green')
print(f"car1 info:{car1}")
#Anything inside {} in an f-string must be converted to a string so Python can combine it with the rest of the text.
# Python sees {car1};car1 is an object of class Carrr
# Python needs a string, so it automatically looks for the __str__ method in the object
print(car1) #works too and called str method