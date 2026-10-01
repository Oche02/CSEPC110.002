print("Welcome to the word guessing game!")
print()

secret_word = "dog"
guess_count = 0
guess = ""

print(f"Your hint is: {' '.join(['_' for _ in range(len(secret_word))])}")

# take user input


# keep asking until the user guesses the secret word correctly
for len(guess) != len(secret_word):
   # guess = input("What is your guess? ")
    print(f"Sorry, the guess must have the same number of letters as the secret word.")

    if len(guess) == len(secret_word):
        print(f"Your hint is: {' '.join([letter if letter in guess else '_' for letter in secret_word])}")
       
    else:
        print("Congratulations! You guessed it!")
        
print(f"It took you {guess_count} guesses.")




# Welcome to the word guessing game!

# Your hint is: _ _ _ _ _ _ 
# What is your guess? temple
# Your hint is: _ _ m _ _ _ 
# What is your guess? moroni
# Your hint is: M O _ o _ i 
# What is your guess? hhhhhh
# Your hint is: h h h h h H 
# What is your guess? mosiah  
# Congratulations! You guessed it!
# It took you 4 guesses.

# Your hint is: _ _ _ _ _ _ 
# What is your guess? nephi
# Sorry, the guess must have the same number of letters as the secret word.

# What is your guess? a
# Sorry, the guess must have the same number of letters as the secret word.

# What is your guess? helaman
# Sorry, the guess must have the same number of letters as the secret word.

# What is your guess? abcdefghijklmnopqrstuvwxyz
# Sorry, the guess must have the same number of letters as the secret word.

# What is your guess? temple
# Your hint is: _ _ m _ _ _ 
# What is your guess? mosiah
# Congratulations! You guessed it!
# It took you 6 guesses.