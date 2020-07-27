'''
This program will take a weight input by the user, then calculate and display the shipping cost.
Programmer: Jacob Roberson
Course: ITM313
'''
print("Welcome to the Shipping Cost Calculator")
weight = eval(input("\nPlease enter the weight of your package in pounds: "))
print("You entered", weight, "lbs")
if(weight <= 0):
    print("\nYou entered an invalid weight.\nPlease rerun the program and enter a weight greater than 0.\nThe following output is invalid:\n")
    shippingCost = 0
elif(weight <= 2 and weight > 0):
    shippingCost = weight * 1.10
elif(weight > 2 and weight <= 6):
    shippingCost = weight * 2.20
elif(weight > 6 and weight <= 10):
    shippingCost = weight * 3.70
else:
    shippingCost = weight * 3.80
print("Your shipping cost will be $%.2f" % (shippingCost))
print("Thank you for using this program")
