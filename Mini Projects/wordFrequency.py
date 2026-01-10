userInput=input("Enter a sentence:").lower().split()

word_count={}
for word in userInput:
    word_count[word]= 1 + word_count.get(word,0) #here get returns 0 if the owrd is not found in the dictonary

print(f"the new word count dictonary is : {word_count}")

for word, count in word_count.items():
    print(f"Word counts:\n{word}:{count}")