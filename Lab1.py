'''
This is a program that asks a user for their name and then greets them.
Next the program asks the user for a radius of a sphere and then
calculates and displays the surface area and volume of the sphere.
Author: Jacob Roberson
Course: ITM313
'''
fullName = input("Please enter your full name: ")
print("Greetings,", fullName + ".\nThanks for using this program!\nThis program will have you enter the radius of a sphere and then will calculate and display the volume and surface area of the sphere.")

radius = eval(input("Please enter the radius of the sphere: "))
volume = ((4/3) * 3.14 * radius * radius * radius)
surfaceArea = (4 * 3.14 * radius * radius)
print("The volume of a sphere with radius %.3f is %.3f" % (radius, volume))
print("The surface area of a sphere with radius %.3f is %.3f" % (radius, surfaceArea))
