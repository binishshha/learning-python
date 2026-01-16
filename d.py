class MyClass:
    def __init__(self):
        self.__private = 10
 
obj = MyClass()
obj.__private=60
print(obj.__private)