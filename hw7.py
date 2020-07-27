'''
This program reads the contents of a txt file with numerical data and then calculates the sum, mean, and median
of the numbers stored in the file. It will also display the smallest and largest values in the set as well as
the number of numbers.
Programmer: Jacob Roberson
Course: ITM313
'''
import os
from statistics import median

f1 = (r"C:\Users\jacob\Desktop\ITM 313\Homework\hw7\data1.txt")
f2 = (r"C:\Users\jacob\Desktop\ITM 313\Homework\hw7\data2.txt")

try:
    os.path.isfile(f1)
    f1open = open(f1, "r")
    f1read = f1open.read()
    nums1 = [eval(x) for x in f1read.split()]
    print("Information on data1.txt:")
    print("The sum is", sum(nums1))
    print("The mean is %.2f" % (sum(nums1)/len(nums1)))
    print("The median is", median(nums1))
    print("The smallest value is", min(nums1))
    print("The largest value is", max(nums1))
    print("There are", len(nums1), "numbers")

    f1open.close()

except FileNotFoundError:
    print("FAILED TO OPEN data1.txt!")

try: 
    os.path.isfile(f2)
    f2open = open(f2, "r")
    f2read = f2open.read()
    nums2 = [eval(y) for y in f2read.split()]
    print("\nInformation on data2.txt:")
    print("The sum is", sum(nums2))
    print("The mean is %.2f" % (sum(nums2)/len(nums2)))
    print("The median is", median(nums2))
    print("The smallest value is", min(nums2))
    print("The largest value is", max(nums2))
    print("There are", len(nums2), "numbers")

    f2open.close()

except FileNotFoundError:
    print("FAILED TO OPEN data2.txt!")



except:
    print("Something went wrong...")

