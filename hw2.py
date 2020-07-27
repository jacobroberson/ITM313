'''
This program provides an interface for users to select a medium and enter a distance
that a sound wave wil travel. Then the program will calculate and display the time it
takes for the waveto travel the given distance.
Programmer: Jacob Roberson
Course: ITM313
'''
#Intialize variables
selection = 0
medium = ""
air = 1100
water = 4900
steel = 16400
distace = 0
time = 0

#Receive user input
print("Welcome to THE SPEED OF SOUND CALCULATOR")
selection = int(input("\nSelect the medium the wave will be traveling through by "
                      "entering the corresponding number\nMENU:\n1.) Air\n2.) Water\n"
                      "3.) Steel\nSELECTION: "))
distance = eval(input("Please enter the distance the sound wave will travel in feet: "))

#Calculation
if(selection == 1 and distance > 0):
    medium = "air"
    time = distance/air
elif(selection == 2 and distance > 0):
    medium = "water"
    time = distance/water
elif(selection == 3 and distance > 0):
    medium = "steel"
    time = distance/steel
elif(distance <= 0):
    print("\nERROR:\nPlease rerun the program and enter a distance greater than 0 feet."
          "\n\nINVALID OUTPUT:")
else:
    print("\nERROR:\nYou have entered an invalid selection. Please rerun the program "
          "and enter a valid selection.\n\nINVALID OUTPUT:")

#Output
print("\nThe time it will take a sound wave to travel", distance, "feet through",
      medium, "is %.4f" % (time), "seconds")



          
        
