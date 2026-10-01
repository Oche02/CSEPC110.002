"""
Author: Augustine Okpe Oche
Program: Adventure Game
"""
# welcome message
print()
space = " "
print(f"{space * 30} ADVENTURE GAME! ")
print("Welcome to the world of adventure! You are about to embark on a journey filled with challenges and excitement. Your choices will determine your fate, so choose wisely. Good luck!")
print()

#collected user input
start = input("Are you ready to start your adventure? (yes/no): ")
start = start.lower()
if start == "yes":
    print("Great! Let's begin your adventure!")
else:
    print("Maybe next time. Goodbye!")

# take the user choises
first_choice = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")
first_choice = first_choice.lower()
if first_choice == "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
elif first_choice == "flashlight":
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    