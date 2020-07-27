'''
This program provides an interface for users to select a type of beam and enter the required
dimesions. Then the program will calculate and display the I value of the beam.
Programmer: Jacob Roberson
Course: ITM313
'''
#Intialize variables
selection = 0
beam = ""
B = 0
H = 0
bOverTwo = 0
b = 0
h = 0
r = 0
I = 0
ans = 'y'

#Intial message
print("Welcome to I value calculator")
while (ans == 'y'):
    selection = int(input("\nSelect the type of beam by entering the corresponding number"
                          "\nMENU:\n1.) I-beam\n2.) Rectangular beam"
                          "\n3.) Cylindrical beam\nSELECTION: "))


#Calculation
    if(selection == 1):
        beam = "I-beam"
        H = eval(input("\nPlease enter the height of the beam in inches: "))
        B = eval(input("Please enter the base width of the beam in inches: "))
        h = eval(input("Please enter the distance between the inside of the flanges "
                       "in inches: "))
        bOverTwo = eval(input("Please enter the distance from the edge of the web to the "
                              "end of the flange in inches: "))
        b = (2 * bOverTwo)
        I = (((B * H**3)-(b * h**3)) / 12)
    elif(selection == 2):
        beam = "rectangular beam"
        h = eval(input("\nPlease enter the height of the beam in inches: "))
        b = eval(input("Please enter the base width of the beam in inches: "))
        I = ((b * h**3) / 12)
    elif(selection == 3):
        beam = "cylindrical beam"
        r = eval(input("\nPlease enter the radius of the beam in inches: "))
        I = ((3.14 * r**4) / 4)
    else:
        print("\nERROR:\nYou have entered an invalid selection. Please rerun the program "
              "and enter a valid selection.\n\nINVALID OUTPUT:")

#Output
    print("\nThe I value of the", beam, "is %.2f" % (I), "in^4")

#Loop
    ans = input("\nWould you like to calculate another I value <y/n>? ")

    if (ans == 'y'):
        selection = 0
        beam = ""
        B = 0
        H = 0
        bOverTwo = 0
        b = 0
        h = 0
        r = 0
        I = 0

#End program message
print("\nThanks for using the I value calculator")



          
        

