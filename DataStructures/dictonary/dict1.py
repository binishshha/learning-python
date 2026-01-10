subjects = {
    "name": ["Artificial Intelligence","DBMS","Computer Ntework"],
    #for assigning more than one value to a key, we can use another datatype like list , tuple, etc
    "level": "4th sem",
    "batch": 2080,
    "code": "CSC200",
    "is_fun": True,
    "batch": 2081, #repeated key 
    "students_marks": #dictonary within a dictonary i.e NESTED DICTIONARY
    {
        "Ram": 99,
        "shyam":44
    }
}

#accessing nested dictonary
print(subjects["students_marks"])
print(subjects["students_marks"]["Ram"])

#prints keys
for k in subjects:
    print(k)

#prints values for each key
for k in subjects:
    print(subjects[k])

#using .keys() method print keys
for k in subjects.keys():
    print(k)

#using .values method
for v in subjects.values():
    print(v)

#using .items method
for k,v in subjects.items():
    print(k,v)

#we can also define nested dictonary differently
students_marks= {
        "Ram": 99,
        "shyam":44
}

subject = {
    "name": ["Artificial Intelligence","DBMS","Computer Ntework"],
    #for assigning more than one value to a key, we can use another datatype like list , tuple, etc
    "level": "4th sem",
    "batch": 2080,
    "code": "CSC200",
    "is_fun": True,
    "batch": 2081, #repeated key 
    "students_marks":students_marks
}

print(subject)