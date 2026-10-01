"""
Author: Augustine Okpe Oche
Program: Comparing numbers and string
"""
print()

#collect user input
first_number = input("What is the first number? ")
second_number = input("What is the second number? ")

#convert to float
first_number = float(first_number)
second_number = float(second_number)

#compare numbers
if first_number > second_number:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if first_number == second_number:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if second_number > first_number:
    print("The second number is greater.")
else:
    print("The second number is not greater.")
print()

#compare strings
favorite_animal = input("What is your favorite animal? ")
favourite_animal = favorite_animal.lower()
if favourite_animal == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")