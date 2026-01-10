#dictonary is a type of data structure in which each item consist of a key-value pair
#every key name should be unique and if not unique the dictonary will return the value of the last added key
#it is modiefieable and ordered
subjects = {
    "name": ["Artificial Intelligence","DBMS","Computer Ntework"],
    #for assigning more than one value to a key, we can use another datatype like list , tuple, etc
    "level": "4th sem",
    "batch": 2080,
    "code": "CSC200",
    "is_fun": True,
    "batch": 2081, #repeated key 
}

#------accessing method------
print(subjects)
print(type(subjects))
print(subjects["name"])
#------can use .get() method too--------
print(subjects.get("name"))
#using get method to specify and call a non existent key wont return key error
print(subjects.get("hairr"))#returns None
# print(subjects["hairr"]) #gives error

print(list(subjects.keys())) #returns all key names
print(list(subjects.values())) #return all values
print(subjects.items()) #returns list of key value pair

#we can add a new keyvalue pair
subjects['teacher']="sanjeev"
print(f"modified dictonary:{subjects}")

#-------------adding method----------
#use .update method to add or modify the dictonary
#you can update multiple keys 
subjects.update({"credit":30, "grade":"A"})#added
subjects.update({"teacher":"ravi"})#modified
print(f"modified dictonary using update method:{subjects}")

#we can chack the existense of any key
if "name" in subjects:
    print(f" \"name\" is present")
else:
    print(f" \"name\" is absent")

#--------removing method--------
#pop() method allows you to pop any one item by specifying keyname
#is case sensitive; key name should be properly specified
subjects.pop("teacher")
print(subjects)

#popitem() removes the last item added
subjects["books"]=1
print(f"after adding: {subjects}")
subjects.popitem()
print(f"after popitem() : {subjects}")

#del keyword
del subjects["batch"] #deletes the batch key
# del subjects #deletes the dictonary
subjects.clear() #empties dictonary but doesnot delete the variable
print(subjects)

#------------copying method------
#using assignment operator = is less effeicient for copying a dictonary 
subjects2=subjects
subjects.update({"batch":2075})
print(f"subjects:{subjects}")
print(f"subjects2:{subjects2}")
#modification in any one of the dictonary automatically modifies the next one too
#so copy method is used
subjects2=subjects.copy()
subjects.update({"batch":2077})
print(f"subjects:{subjects}")
print(f"subjects2:{subjects2}")

#we can also use another methos for copying
subjects3=dict(subjects)
subjects.update({"batch":2079})
print(f"subjects:{subjects}")
print(f"subjects2:{subjects2}")

#we can also construct a dictonary variable using dict constructor
#we use = for differentiating key and value
#we cannot start a keyname with number,space and special character 
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