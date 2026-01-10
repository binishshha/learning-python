dictonary={
    "abhor": "To feel hatred or disgust for something",
    "bigot": "A person who is intolerant of others' views or beliefs",
    "enigma" : "A person or thing that is mysterious or puzzling",
    "search for": "More formal", #if you use dict to create dictonary you cannot use spaces in key name
    "placid": "Calm and peaceful, with little movement or activity",
    "resilient": "Able to withstand or recover quickly from difficult conditions"
}

word= input("Enter a word:").lower() # lower enables your input to not care about the cases i.e makes it case insensitive

if word in dictonary:
    print(f"the meaning of {word} is : {dictonary.get(word)}") #you can use {dictonary[word]} too and not get method
else:
    print(f"{word} not found in dictonary")