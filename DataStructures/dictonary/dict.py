#dictonary is a type of data structure in which each item consist of a key-value pair
#every key name should be unique and if not unique the dictonary will return the value of the last added key
#it is modiefieable and ordered
subjects = {
    "name": "Artificial Intelligence",
    "level": "4th sem",
    "batch": 2080,
    "code": "CSC200",
    "is_fun": True,
    "batch": 2081, #repeated key 
    "students_marks": #dictonary within a dictonary
    {
        "Ram": 99,
        "shyam":44
    }
}

#------accessing method------
print(subjects)
print(type(subjects))
print(subjects["name"])
print(subjects["students_marks"])
print(subjects["students_marks"]["Ram"])
print(list(subjects.keys()))
print(list(subjects.values()))
print(subjects.items())

#we can also construct a dictonary variable using dict constructor
#we use = for differentiating key and value
#we cannot use number,space and special character as a keyname
subject = dict(
    name= "Artificial Intelligence",
    level= "4th sem",
    batch= 2080,
    code="CSC200",
    _is_fun= True,
    # batch=2081, #repeated key (cannot keep duplicate keyname while using 'dict' ;throws error)
    students_marks=
    {
        "Ram": 99,
        "shyam": 44
    },
)
print(subject)