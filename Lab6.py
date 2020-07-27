'''
This program takes up to 10 numerical inputs until the user enters -9999 to stop the input.
If the user stops the input before entering any numbers, an error is displayed. Otherwise,
the entered values are displayed along with their distance from the average of all the numbers
entered.
Name: Jacob Roberson
Course: ITM313
'''
num = []
i = 0
total = 0
count = 0
index = 0
distance = []

i = eval(input("Enter up to 10 numbers. Enter -9999 to end input: "))
while(i != -9999 and count < 10):
    num.append(i)
    count += 1

    #Read the next number
    i = eval(input("Enter a number. Enter -9999 to end input: "))

if (count == 0):
    print("ERROR: No numbers are entered except -9999")
else:
    total = sum(num)
    avg = total / count
    for r in num:
        d = (num[index] - avg)
        distance.append(d)
        index += 1
        r += 1
    print("\nOutput: (number, distance from the average)")
    for (num, distance) in enumerate(zip(num, distance)):
        print(distance)
