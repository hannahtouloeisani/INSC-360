# Author: Hannah Touloeisani
# Date: 2-24-20
# Description: Assignment 4

import random
print('*'*56)
random_num = random.randint(1,10)
print("* A random number between 1 and 10 has been generated." +\
    " Can you guess what it is?")
entry = input("Enter a number: ")
print("You entered: {}".format(entry))


#Input validation

if entry.isnumeric():
    entry = int(entry)
else:
    print('Please enter a number 1-10')

#Compare against compter selection

while random_num <11:
    print('Take another guess.')
    guess = input()
    guess = int(guess)

    random_num = random_num + 1

#Responding to each condition

    if guess < random_num:
        print('Your guess is too low')
    if guess > random_num:
        print("Your guess is too high")
    if guess == random_num:
        break

if guess == random_num:
    print('Congrats! You guessed my number.')




