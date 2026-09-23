"""
Added three more adventure levels with more than two(2) choices in 3 scinarios, allowing the player to progress through Level 5.
Improved the game flow so choosing "no" from thee start ends the adventure, while choosing "yes" continue start the story to the end point of every choises made.

Author: Augustine Okpe Oche
Program: Adventure Game
"""

# welcome message
print()
spacing = " "
print(f"{spacing * 50} ADVENTURE GAME! ")
print("Welcome to the world of adventure! Your choices will determine your fate, so choose wisely. Good luck!")
print()

# collected user input
start_game = input("Are you ready to start your adventure? (yes/no): ")
start_game = start_game.lower()

if start_game == "yes":
    print()
    print(f"{spacing * 40}Great! Let's begin your adventure!")
    print()

    # LEVEL 1
    item_choice = input("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ")
    item_choice = item_choice.lower()

    if item_choice == "match":
        print()
        bear_choice = input("You strike the match and see a large grizzly bear. Do you want to RUN or HIDE behind a tree? ")
        bear_choice = bear_choice.lower()

        if bear_choice == "run":
            print()
            print("You run as fast as you can, but the bear is faster. The bear catches you. Game over.")

        elif bear_choice == "hide":
            print
            print("You hide behind a tree. The bear loses interest and walks away. You are safe for now.")

            # LEVEL 3
            river_choice = input("You continue through the forest and discover a RIVER. Do you want to use the BRIDGE or the BOAT? ")
            river_choice = river_choice.lower()

            if river_choice == "bridge":
                print()
                print("You carefully cross the old bridge and make it safely to the other side.")

                # LEVEL 4
                forest_route_choice = input("You discover a mysterious CAVE and a narrow PATH leading up a hill. Do you choose the CAVE or PATH? ")
                forest_route_choice = forest_route_choice.lower()

                if forest_route_choice == "cave":
                    print()
                    print("You enter the cave, but rocks fall behind you and block the entrance. Game over.")

                elif forest_route_choice == "path":
                    print()
                    print("You follow the path up the hill and see lights in the distance.")

                    # LEVEL 5
                    village_choice = input("You reach a village with a locked gate. Do you TALK to the guard or enter the TUNNEL? ")
                    village_choice = village_choice.lower()

                    if village_choice == "talk":
                        print()
                        print("The guard believes your story and opens the gate. Congratulations! You completed the adventure!")

                    elif village_choice == "tunnel":
                        print()
                        print("You enter the tunnel but reach a dead end and become trapped. Game over.")

                    else:
                        print()
                        print("Invalid choice. Please choose TALK or TUNNEL.")

                else:
                    print()
                    print("Invalid choice. Please choose CAVE or PATH.")

            elif river_choice == "boat":
                print()
                print("The river current becomes too strong. The boat crashes into a rock. Game over.")

            else:
                print()
                print("Invalid choice. Please choose BRIDGE or BOAT.")

        else:
            print()
            print("Invalid choice. Please choose RUN or HIDE.")

    # LEVEL 2
    elif item_choice == "flashlight":
        print()
        path_choice = input("You turn on the flashlight and hear something in the trees. Do you want to FOLLOW the path or LOOK in the trees? ")
        path_choice = path_choice.lower()

        if path_choice == "follow":
            print()
            print("You follow the path and find a small cabin. You are safe for now.")

            # LEVEL 3
            cabin_choice = input("Inside the cabin, you find a locked CHEST and a DOOR. Do you examine the CHEST or open the DOOR? ")
            cabin_choice = cabin_choice.lower()

            if cabin_choice == "chest":
                print()
                print("You find a key and open the chest. Inside, you discover a map showing a safe route out of the forest.")

                # LEVEL 4
                travel_route_choice = input("The map shows a MOUNTAIN trail and a VALLEY road. Do you choose MOUNTAIN or VALLEY? ")
                travel_route_choice = travel_route_choice.lower()

                if travel_route_choice == "mountain":
                    print()
                    print("A dangerous storm begins on the mountain. You are forced to turn back. Game over.")

                elif travel_route_choice == "valley":
                    print()
                    print("You follow the valley road and reach the edge of the forest.")

                    # LEVEL 5
                    traveler_choice = input("You find an injured TRAVELER. Do you HELP the traveler or CONTINUE toward safety? ")
                    traveler_choice = traveler_choice.lower()

                    if traveler_choice == "help":
                        print()
                        print("You help the traveler, and he shows you a safe shortcut. Congratulations! You completed the adventure!")

                    elif traveler_choice == "continue":
                        print()
                        print("You continue alone, take the wrong road, and become lost again. Game over.")

                    else:
                        print()
                        print("Invalid choice. Please choose HELP or CONTINUE.")

                else:
                    print()
                    print("Invalid choice. Please choose MOUNTAIN or VALLEY.")

            elif cabin_choice == "door":
                print()
                print("You open the door and discover a wild animal inside. It attacks before you can escape. Game over.")

            else:
                print()
                print("Invalid choice. Please choose CHEST or DOOR.")

        elif path_choice == "look":
            print()
            print("You see glowing eyes in the trees and quickly turn back toward the path.")

            # LEVEL 3
            direction_choice = input("You reach a fork in the path. Do you go toward the HILL or the STREAM? ")
            direction_choice = direction_choice.lower()

            if direction_choice == "hill":
                print()
                print("You climb the hill and find an abandoned watchtower.")

                # LEVEL 4
                watchtower_choice = input("From the watchtower, you see a ROAD and a CAMPFIRE. Do you choose ROAD or CAMPFIRE? ")
                watchtower_choice = watchtower_choice.lower()

                if watchtower_choice == "road":
                    print()
                    print("You reach the road and see signs pointing toward a nearby town.")

                    # LEVEL 5
                    vehicle_choice = input("A vehicle approaches. Do you WAVE for help or HIDE until it passes? ")
                    vehicle_choice = vehicle_choice.lower()

                    if vehicle_choice == "wave":
                        print()
                        print("The driver stops and gives you a ride to town. Congratulations! You completed the adventure!")

                    elif vehicle_choice == "hide":
                        print()
                        print("The vehicle passes. Night falls and you become lost again. Game over.")

                    else:
                        print()
                        print("Invalid choice. Please choose WAVE or HIDE.")

                elif watchtower_choice == "campfire":
                    print()
                    print("You approach the campfire and hear footsteps surrounding you in the darkness. Game over.")

                else:
                    print()
                    print("Invalid choice. Please choose ROAD or CAMPFIRE.")

            elif direction_choice == "stream":
                print()
                print("You follow the stream, but become stuck in the muddy ground. Game over.")

            else:
                print()
                print("Invalid choice. Please choose HILL or STREAM.")

        else:
            print()
            print("Invalid choice. Please choose FOLLOW or LOOK.")

    else:
        print()
        print("Invalid choice. Please choose MATCH or FLASHLIGHT.")

elif start_game == "no":
    print("Maybe next time. Goodbye!")
    print()

else:
    print("Invalid choice. Please enter YES or NO.")
    print()
