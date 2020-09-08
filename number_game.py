# create two player number guessing game

import sys
import time
import random

# define variables
score = 0
score1 = 0
target = 2

while 1:
    number = random.randint(1, 5)

    print("*Guess Any Number Between 1 to 5*")
    print("")
    guess = int(input("Player One : "))
    guess1 = int(input("Player Two : "))

    print("")
    print("The number was ", number)
    print("")

    if guess == number:
        score = score + 1
        print("Player One Score : ", score)
        print("Player Two Score : ", score1)

    elif guess1 == number:
        score1 = score1 + 1
        print("Player Two Score : ", score1)
        print("Player One Score : ", score)

    else:
        print("")
        print("None of the Guesses were Correct")

    if score == target:
        print("")
        print("Player One has Won the Game.")
        sys.exit()

    elif score1 == target:
        print("")
        print("Player Two has Won the Game.")
        sys.exit()
