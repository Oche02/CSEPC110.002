# I added three more inputs for a place, a strange object, and a food.
# I used these new words in the story to make the adventure more detailed.

"""
Program: Clever stories
Author: Augustine Okpe Oche
"""

adjective = input("Enter an adjective, such as tall or glowing: ")
animal = input("Enter an unusual animal, such as a unicorn or dragon: ")
verb1 = input("Enter a past-tense verb, such as ran or jumped: ")
exclamation = input("Enter an exclamation, such as Wow or Oh no: ")
verb2 = input("Enter a verb, such as dance or sing: ")
verb3 = input("Enter another verb, such as laugh or cry: ")
place = input("Enter a place, such as a castle or spaceship: ")
object_name = input("Enter a strange object, such as a banana phone: ")
food = input("Enter a food, such as pizza or tacos: ")

print()
print("Your Story is:")
print()
print("The other day, I was really in trouble at the " + place + " when a")
print(adjective + " " + animal + " " + verb1 + " down the hallway." + ' "' + exclamation.capitalize() + '!"' + " I yelled. But all")
print("I could think to do was to " + verb2 + " with a " + object_name + " over and over.")
print("Miraculously, that caused it to stop, but not before it tried to " + verb3)
print("right in front of my family, who were eating " + food + ".")