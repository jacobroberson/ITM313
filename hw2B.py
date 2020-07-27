'''
This program will receive input on two class grades and correspoding credit hours, then it will calculate and display the student's GPA.
Programmer: Jacob Roberson
Course: ITM313
'''
#input
print("Welcome to the GPA Calculator\n")
grade1 = input("Please enter the letter grade you received in your first class ('A, B, C, D, or F'): ")
credit1 = int(input("Please enter the credit hours for your first class: "))
grade2 = input("Please enter the letter grade you received in your second class ('A, B, C, D, or F'): ")
credit2 = int(input("Please enter the credit hours for your second class: "))

#calculations
if(grade1 == "A"):
    score1 = 4.0
elif(grade1 == "B"):
    score1 = 3.0
elif(grade1 == "C"):
    score1 = 2.0
elif(grade1 == "D"):
    score1 = 1.0
elif(grade1 == "F"):
    score1 = 0.0

if(grade2 == "A"):
    score2 = 4.0
elif(grade2 == "B"):
    score2 = 3.0
elif(grade2 == "C"):
    score2 = 2.0
elif(grade2 == "D"):
    score2 = 1.0
elif(grade2 == "F"):
    score2 = 0.0

GPA = (((score1 * credit1) + (score2 * credit2)) / (credit1 + credit2))

#output
if(score1 < score2):
    print("\nYour lowest grade was a(n)", grade1, "in your first class which was", credit1, "credit hours")
    print("Your highest grade was a(n)", grade2, "in your second class which was", credit2, "credit hours")
    print("Your GPA is a %.2f" % GPA)
    if(GPA < 2.00):
        print("Warning: Your GPA is less than 2.00")
    if(GPA >= 3.50):
        print("Congratulations, your GPA is greater than or equal to 3.50")

elif(score2 < score1):
    print("\nYour lowest grade was a(n)", grade2, "in your second class which was", credit2, "credit hours")
    print("Your highest grade was a(n)", grade1, "in your first class which was", credit1, "credit hours")
    print("Your GPA is a %.2f" % GPA)
    if(GPA < 2.00):
        print("Warning: Your GPA is less than 2.00")
    if(GPA >= 3.50):
        print("Congratulations, your GPA is greater than or equal to 3.50")


else:
    print("\nYou received the same grade in both classes")
    print("Your grade was a(n)", grade1, "in your first class which was", credit1, "credit hours")
    print("Your grade was a(n)", grade2, "in your second class which was", credit2, "credit hours")
    print("Your GPA is a %.2f" % GPA)
    if(GPA < 2.00):
        print("Warning: Your GPA is less than 2.00")
    if(GPA >= 3.50):
        print("Congratulations, your GPA is greater than or equal to 3.50")
