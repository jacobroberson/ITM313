'''
This program takes integer inputs until the user enters -9999 and
then calculates and displays the smallest number entered, the largest
number entered, the total, and the average
Name: Jacob Roberson
Course: ITM313
'''
num = []
i = 0
total = 0
count = 0

i = int(input("Enter an integer. Enter -99999 to end input: "))
while(i != -99999):
    num.append(i)
    count += 1

    #Read the next number
    i = int(input("Enter an integer. Enter -99999 to end input: "))

if (count == 0):
    print("No numbers are entered except -99999")
else:
    small = min(num)
    large = max(num)
    total = sum(num)
    print("The smallest number is", small)
    print("The largest number is", large)
    print("The total is", total)
    print("The average is", total / count)
