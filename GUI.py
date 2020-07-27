'''
This program uses a GUI to ask a user to enter information about themselves as well as enter
two numbers. Then the program will run calculations with those numbers and display all the
information generated.
Programer: Jacob Roberson
Course: ITM 313
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("Type your full name", "Enter your name")
result = "Your name is: " + name

major = simpledialog.askstring("Type your field major", "Enter your major")
result = result + "\n" + "Your major is: " + major

semester = simpledialog.askinteger("Input the number of semesters you've been in school",
                                   "Enter number of semesters")
result = result + "\n" + "Number of semesters: " + str(semester) + "\n"

num1 = simpledialog.askfloat("Input a number", "Enter number")
result = result + "\n" + "Number 1: " + str(num1) + "\n"

num2 = simpledialog.askfloat("Input another number", "Enter number")
result = result + "Number 2: " + str(num2) + "\n"

summation = num1 + num2
result = result + "Sum of Number 1 and Number 2: " + str(summation) + "\n"

product = num1 * num2
result = result + "Product of Number 1 and Number 2: " + str(product) + "\n"

messagebox.showinfo("Display Results", result)
