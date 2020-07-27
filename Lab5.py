'''
This program will accept input for the length of the sides of a triangle, determine
whether the input is valid, and then calculate the area of the triangle. If the input
is invalid, the program will notify the user.
Programmer: Jacob Roberson
Course: ITM313
'''
import math


# Displays greeting
def greeting():
    print("Welcome to the area of a triangle calulator\n")


# Displays closing
def closing():
    print("\nThank you for using the area of a triangle calculator")


# Returns true if the sum of any two sides is greater than the third side
def isValid(side1, side2, side3):
    if (side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1):
        validity = 1
    else:
        validity = 0
    return validity


# Returns the area of the triangle
def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    triArea = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return triArea

def main():
    greeting()
    side1 = eval(input("Please enter the length of the first side of the triangle: "))
    side2 = eval(input("Please enter the length of the second side of the triangle: "))
    side3 = eval(input("Please enter the length of the third side of the triangle: "))
    validity = isValid(side1, side2, side3)
    if (validity == 1):
        triArea = area(side1, side2, side3)
        print("\nThe area of a triange with side lengths", side1, ",", side2, ",",
              side3, "is", triArea)
    if (validity == 0):
        print("\nYou entered invalid side lengths, please rerun the program")
    closing()


# start program
main()
