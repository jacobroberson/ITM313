'''
This is a program that creates three classes- Circle, Square, and Rectangle- that are used
to display the class name as well as calculate the area of the corresponding shape. A
random number generator and a loop are then used to create objects of the classes at random
that populate a list.
Programmer: Jacob Roberson
Course: ITM 313
'''
import math
import random
class Circle:
    def __init__(self, radius = 2):
        self.__radius = radius

    def accessor(self):
        print("Radius: " + str(self.__radius) + "cm")

    def mutator(self, radius):
        self.__radius = radius

    def find_area(self):
        area = math.pi*(self.__radius**2)
        self.__area = area

    def display(self):
        print("Object type: Circle")
        print("Area: " + str(self.__area) + "cm^2")

class Square:
    def __init__(self, side = 2.5):
        self.__side = side

    def accessor(self):
        print("Side length: " + str(self.__side) + "cm")

    def mutator(self, side):
        self.__side = side

    def find_area(self):
        area = self.__side**2
        self.__area = area

    def display(self):
        print("Object type: Square")
        print("Area: " + str(self.__area) + "cm^2")

class Rectangle:
    def __init__(self, length = 9, width = 10):
        self.__length = length
        self.__width = width

    def accessor(self):
        print("Length: " + str(self.__length) + "cm")
        print("Width: " + str(self.__width) + "cm")

    def mutator(self, length, width):
        self.__length = length
        self.__width = width

    def find_area(self):
        area = self.__length * self.__width
        self.__area = area

    def display(self):
        print("Object type: Rectangle")
        print("Area: " + str(self.__area) + "cm^2")

def main():
    shapes = [0,0,0,0,0,0,0,0,0,0]
    count = [0,1,2,3,4,5,6,7,8,9]
    print("This program creates a list of 10 shapes at random and displays "
          "the object type as well as the area of the object based off of "
          "either the default values or user input.")
    print("DEFAULT VALUES:\nRadius: 2cm\nSide length: 2.5cm\nLength: 9cm"
          "\nWidth: 10cm\n")
    for i in count:
        choice = random.randrange(1,4)
        if (choice == 1):
            shapes[i] = Circle()
            print("Shape number", str(i+1), ": Circle")
            change = input("Would you like to alter the radius? (y/n)")
            if(change == "y"):
                alteration = eval(input("Enter new radius: "))
                shapes[i].mutator(alteration)
            print("\n")
        if (choice == 2):
            shapes[i] = Square()
            print("Shape number", str(i+1), ": Square")
            change = input("Would you like to alter the side length? (y/n)")
            if(change == "y"):
                alteration = eval(input("Enter new side length: "))
                shapes[i].mutator(alteration)
            print("\n")
        if (choice == 3):  
            shapes[i] = Rectangle()
            print("Shape number", str(i+1), ": Rectangle")
            change = input("Would you like to alter the length and width? (y/n)")
            if(change == "y"):
                alter1 = eval(input("Enter new length: "))
                alter2 = eval(input("Enter new width: "))
                shapes[i].mutator(alter1, alter2)
            print("\n")

    for i in count:
        shapes[i].find_area()
        shapes[i].accessor()
        shapes[i].display()
        print("\n")
       
main()
