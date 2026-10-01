"""
Activity Instructions

Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

1. Write a Python Program that does each of the following:

Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number. For example:


    Please type a positive number: -3
    Sorry, that is a negative number. Please try again.
    Please type a positive number: -8
    Sorry, that is a negative number. Please try again.
    Please type a positive number: -1
    Sorry, that is a negative number. Please try again.
    Please type a positive number: 12
    The number is: 12

"""
number = int(input("Please type a positive number: "))
while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")


"""


Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you." For example:


May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? no
May I have a piece of candy? yes
Thank you.

"""

candi = " "
candi = candi.lower()
while candi != "yes":
    candi = input("May I have a piece of candy? ")
print("Thank you.")