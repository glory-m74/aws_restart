print("Welcome to guess the Number!")
print("The rules are simple. i will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isguessright = false
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))