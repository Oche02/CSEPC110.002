import random

play_again = "yes"

# keep playing the game as long as the user says "yes" when asked if they want to play again
while play_again == "yes":

# keep asking until the user guesses the magic number correctly
    guess = -1
    guess_count = 0
    magic_number = random.randint(1, 100)

    while guess != magic_number:
        guess = int(input("What is your guess? "))
        guess_count = guess_count + 1
    
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print("You guessed it!")
    
    # print the number of guesses it took the user to guess the magic number
    print(f"It took you {guess_count} guesses")

    # ask the user if they want to play again
    play_again = input("Would you like to play again (yes/no)? ")
    
# print a goodbye message when the user chooses not to play again
print("Thank you for playing. Goodbye.")

