'''
This program counts the number of positive or negative numbers entered.
Print sum and average of numbers.
Debugging a program Assignment.
Name: Jacob Roberson
'''

countPositive = 0
countNegative = 0
total = 0
count = 0

num = int(input("Enter an integer. Enter 0 to end input: "))
while(num != 0):
    if (num > 0):
        countPositive += 1
        total += num
        count += 1
    elif (num < 0):
        countNegative += 1
        total += num
        count += 1

    #Read the next number
    num = int(input("Enter an integer. Enter 0 to end input: "))

if (count == 0):
    print("No numbers are entered except 0")
else:
     print("The number of positives is", countPositive)
     print("The number of negatives is", countNegative)
     print("The total is", total)
     print("The average is", total / count)

