# This program gives a range to the user to guess a number

# import random number for the computer to generate
import random

# Give the user the range and get input from the user
guessed_number = int(input("Guess a number between 1 and 10: "))

#set random int between 1 and 10
random_number = random.randint(1, 10)

#have the user loop until they guess the correct number
#provide feedback if too high or low

while guessed_number != random_number:
    if guessed_number > random_number:
        print("You guessed too high")
        guessed_number = int(input("Guess again: "))
    else:
        print("You guessed too low")
        guessed_number = int(input("Guess again: "))

print("Correct")