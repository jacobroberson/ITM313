'''
This program provides an interface for users to select a type of beam and enter the required
dimesions. Then the program will calculate and display the I value of the beam.
Programmer: Jacob Roberson
Course: ITM313
'''

# Displays greeting
def greeting():
    print("Welcome to I value calculator")

# Displays closing
def closing():
    print("\nThanks for using the I value calculator")

# Gets selection
def selection():
    s = int(input("\nSelect the type of beam by entering the corresponding number"
                          "\nMENU:\n1.) I-beam\n2.) Rectangular beam"
                          "\n3.) Cylindrical beam\nSELECTION: "))
    return s

# Calculates I-beam
def iBeam():
    beam = "I-beam"
    H = eval(input("\nPlease enter the height of the beam in inches: "))
    B = eval(input("Please enter the base width of the beam in inches: "))
    h = eval(input("Please enter the distance between the inside of the flanges "
                   "in inches: "))
    bOverTwo = eval(input("Please enter the distance from the edge of the web to the "
                          "end of the flange in inches: "))
    b = (2 * bOverTwo)
    I = (((B * H**3)-(b * h**3)) / 12)
    return beam, I

# Calculates rectangular beam
def recBeam():
    beam = "rectangular beam"
    h = eval(input("\nPlease enter the height of the beam in inches: "))
    b = eval(input("Please enter the base width of the beam in inches: "))
    I = ((b * h**3) / 12)
    return beam, I

# Calculates cylindrical beam
def cylBeam():
    beam = "cylindrical beam"
    r = eval(input("\nPlease enter the radius of the beam in inches: "))
    I = ((3.14 * r**4) / 4)
    return beam, I

# Displays error
def error():
     print("\nERROR:\nYou have entered an invalid selection. Please rerun the program "
           "and enter a valid selection.\n\nINVALID OUTPUT:")

# main
def main():
    greeting()
    ans = 'y'
    beam = "beam"
    I = 0
    while (ans == 'y'):
        s = selection()
        if (s == 1):
            beam, I = iBeam()
        elif (s == 2):
            beam, I = recBeam()
        elif (s == 3):
            beam, I = cylBeam()
        else:
            error()
        print("\nThe I value of the", beam, "is %.2f" % (I), "in^4")
        ans = input("\nWould you like to calculate another I value <y/n>? ")
    closing()

# start program
main()
