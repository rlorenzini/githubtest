#random number 1-9
#guess number
#tell user if too high, low, or right
#count guesses and times correct
#quit by typing 'exit'
#number = random.randint(1,9)

import random

number = random.randint(1,9)
guess = 0
count = 0


while guess != number and guess != "exit":
    guess = input("What's your guess?")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you",count,"tries!")
