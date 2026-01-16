#---------STUDENT GRADE MANAGEMENT SYSTEM-----------

class Students:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__grade=[]

    def addGrade(self,*grade): #*grade use garesi chai arbitary positional parameter huncha
        # we can pass any number of grades we want as a tuple
        # so for loop is used
        for i in grade:
           if 0<=i<=100:
              self.__grade.append(i)
           else:
              print("wrong grade update!!")

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