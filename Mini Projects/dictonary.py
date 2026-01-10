dictonary={
    "abhor": "To feel hatred or disgust for something",
    "bigot": "A person who is intolerant of others' views or beliefs",
    "enigma" : "A person or thing that is mysterious or puzzling",
    "joyful": "full of joy",
    "search for": "More formal", #if you use dict to create dictonary you cannot use spaces in key name
    "placid": "Calm and peaceful, with little movement or activity",
    "resilient": "Able to withstand or recover quickly from difficult conditions",
    "happy":"full of joy",
}

word= input("Enter a word:").lower() # lower enables your input to not care about the cases i.e makes it case insensitive

if word in dictonary:
    print(f"the meaning of {word} is : {dictonary.get(word)}") #you can use {dictonary[word]} too and not get method
else:
    print(f"{word} not found in dictonary")

#PROBLEM: we have a dictonary with unique keyname but same values for different keyname
#SOLUTION: remove duplicate values in a dictinary
new_dictionary={}
for k,v in dictonary.items():
        if v not in new_dictionary.values():
            # new_dictionary[k]=v #this can be sued to add item too
            new_dictionary.update({k:v})

print(new_dictionary) #dictonary without duplicte values