# encapsulation is a property in oop that allows us to provide controlled access todata using methods like getter and setter
# it hides internal details from outside access
# eg creates a private attribute that hides that cannot be accessed from putside the class

#---------STUDENT GRADE MANAGEMENT SYSTEM-----------

class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__grade=[] #private attribute

    #getter method
    def addGrade(self,*grade): #*grade use garesi chai arbitary positional parameter huncha
        # we can pass any number of grades we want as a tuple
        # so for loop is used
        for i in grade:
           if 0<=i<=100:
              self.__grade.append(i)
           else:
              print("wrong grade update!!")

    #setter method
    def averageGrade(self):
        if len(self.__grade)>0:
            return sum(self.__grade)/len(self.__grade)
        else:
            return 0 
        
    def displayInfo(self):
        print(f"Student Name: {self.name}")
        print(f"Student age: {self.age}")
        print(f"Grades: {self.__grade}")
        print(f"Average of grades: {self.averageGrade()}")  #we can also call a function inside class using self 

student1=Students("ram",20)
student1.addGrade(10,20,30)
student1.displayInfo()

# student1.__grade(1000000) #generates an attribute error because this grade attribute cannot be accessed from here
student1.__grade=[1000000.-1000] #changing gardes like this wont matter now because __grade is seen as a new attribute for this obj now
# and this value wont be passed to out object student1
student1.displayInfo()