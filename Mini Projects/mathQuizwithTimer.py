import random

def generate_questions():
    number1=random.randint(1,10)
    number2=random.randint(1,10)
    operator=random.choice(['+','-','*','**'])

    if operator=='+':
        result=number1+number2
        question=(f"{number1}+{number2}")
    
    elif operator=='-':
        result=number1-number2
        question=(f"{number1}-{number2}")

    elif operator=='*':
        question=(f"{number1}*{number2}")
        result=number1*number2

    elif operator=='**':
        result=number1**number2
        question=(f"{number1}**{number2}")

    return question,result

import datetime as dt

def game():
    num_of_questions=random.randint(1,10)
    score=0
    start_time=dt.datetime.now()

    for i in range(1,num_of_questions+1):
        question,result=generate_questions()
        print(question)
        answer=float(input("Enter the answerr:"))
        if (answer==result):
            score+=1
            print("OMG CORRECT!!!!!")
        else:
            print(f"OOPS WRONG\nThe correct answer is:{result}\nTRY Next one")

    end_time=dt.datetime.now()
    time_taken=end_time-start_time
    print(f"TOTAL SCORE:{score}")
    print(f"Time Take:{time_taken.total_seconds()} seconds")
    if score>(num_of_questions/2):
        print("GOOD GAME!!!!")
    else:
        print("BETTER LUCK NEXT TIME!")

game()