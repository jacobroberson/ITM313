'''
This program will help a student learn basic multiplication by generating two single
digit random integers and asking the user to input the answer until they get it correct.
Programmer: Jacob Roberson
Course: ITM313
'''
import random

# create random number between 1 and 9
num1 = random.randint(1, 9)
num2 = random.randint(1, 9)
guess = 0
multi = num1 * num2
ans = 'y'
print("Welcome to Multiplication Machine\n")

while (ans == 'y'):
    while (guess != multi):
        print("How much is", num1, "times", num2, "?")
        guess = int(input())

        if (guess == multi):
            print("Very Good!")

        else:
            print("No. Please try again")

    ans = input("Would you like to try another problem <y/n>? ")

    if (ans == 'y'):
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        multi = num1 * num2

print("Thanks for learning")
