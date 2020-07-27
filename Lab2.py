'''
This program determines a students grade level based off of the number of credits they
have.
Programmer: Jacob Roberson
Course: ITM313
'''
credits = eval(input("Please enter the number of credit hours the student has completed: "))
if (credits >= 0 and credits < 32):
    print("This student is a 1st Year Student")
elif (credits >= 32 and credits <= 63):
    print("This student is a 2nd Year Student")
elif (credits >= 64 and credits <= 95):
    print("This student is a 3rd Year Student")
elif (credits >= 96):
    print("This student is a 4th Year Student")

print("Thank you for using this program")
