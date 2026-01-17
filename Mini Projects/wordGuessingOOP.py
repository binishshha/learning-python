#create a word guessing game where user can guess a word muliplt times and count attempts too

import random

class Game:
    def __init__(self):
        self.__secretkey=random.randint(1,100)
        self.__attempts=0

    def check_key(self,key):
        self.__attempts+=1
        if key<self.__secretkey:
            return "GUESS HIGHER KEYS"
        elif key>self.__secretkey:
            return "GUESS LOWER"
        else:
            return "CORRECT GUESS OMGG"
    
    def check_attempts(self):
        return self.__attempts
    
    def reset_game(self):
        self.__secretkey=random.randint(1,100)
        self.__attempts=0
        

guess=Game()

while True:
    key=int(input("Guess anumber between 1 to 100:"))
    result=guess.check_key(key)
    print(result)

    if result=="CORRECT GUESS OMGG":
        print(f"Guessed correct in {guess.check_attempts()} attempts")
        replay=input("Do you want to play again(Y/N)?").lower()
        if replay=="y":
            guess.reset_game()
            # guess.secret=random.randint(1,100) #we could have done thsi too if the secret keys werrenot priveate buut we must keep them private
        else:
            break