#take user inputs
men = input("numbers of men: ")
women = input("numbers of women: ")
men = int(men)
women = int(women)
total = men + women

# number_of_players = total >= 7
# number_of_women = women >= 4

has_enough_players = total >= 7
has_enough_women = women >= 4

#result of the comparison
if has_enough_players and has_enough_women:
    print("The team is ready to play.")
else:
    print("The team is not ready to play a legal game.")    
if not has_enough_players:
    print("ask the other team if they want to practice.")
    
# if number_of_players >= 7:
#     print("The number of players is complete.")
# else:
#     print("The number of players is not complete.")
# if number_of_women >= 4:
#     print("There are enough women on the team.")
# else:
#     print("There are not enough women on the team.")
#     print("We can only practice with the available players.")
