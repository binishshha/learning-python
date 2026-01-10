#Ask user to enter a sentence
# Calculate the character frequency
# Show the result like this in the output:'c' => 10, 'b' => 15

userInput=input("Enter a sentence:").lower()

characterfreq={}
for char in userInput:
    if char.isalpha():
        characterfreq[char]=1 + characterfreq.get(char,0)

print(characterfreq)

for char, count in characterfreq.items():
    print(f"'{char}' => {count}")