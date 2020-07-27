'''
This a program that will create a Pet class which will contain name,
animal type, and age attributes. This program will allow the user to enter a
name, animal type, and age and use the Pet class to create an object and display
the corresponding attributes.
Programmer: Jacob Roberson
Course: ITM313
'''
class Pet:
    def __init__(self, name = "", animal_type = "", age = 0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self,age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

name = input("Please enter your pet's name: ")
animal_type = input("Please enter the type of animal your pet is: ")
age = eval(input("Please enter your pet's age: "))


pet1 = Pet(name, animal_type, age)

print("\nName:", pet1.get_name())
print("Animal Type:", pet1.get_animal_type())
print("Age:", pet1.get_age())
