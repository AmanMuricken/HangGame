import random
name=input("What is your name:")
print("Good luck",name)
words=["carrot","bed","hands","kitchen","television","computer","mobile","buildings","rubber","horse"]
r=random.choice(words)
print("Guess the charaters of the word")
guesses=""
turns=12
while turns>0:
    failed=0
    for i in r:
        if i in guesses:
            print(i)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You win")
        print("The word is",r)
        break
    guess=input("Guess the character:")
    guesses+=guess
    if guess not in r:
        turns-=1
        print("wrong")
        print("You have",turns,"chances left")
        if turns==0:
            print("You losse better luck next time!")
        
