## Extra features: type "hint" to reveal the first and last letters, or "quit" to reveal the word and exit.
print("Welcome to the word guessing game!")
print()

secret_word = "mosiah"
guess_count = 0
guess = ""
print("Your hint is:", " ".join(["_" for _ in range(len(secret_word))]))

while guess != secret_word:
    guess = input("What is your guess? ").strip().lower()

    if guess == "hint":
        print(f"Extra hint: the word starts with '{secret_word[0]}' and ends with '{secret_word[-1]}'.")
        continue

    if guess == "quit":
        print(f"The secret word was {secret_word}.")
        break

    guess_count += 1

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
        continue

    if guess == secret_word:
        print("Congratulations! You guessed it!")
    else:
        hint = []
        for index, letter in enumerate(guess):
            if letter == secret_word[index]:
                hint.append(letter.upper())
            elif letter in secret_word:
                hint.append(letter.lower())
            else:
                hint.append("_")
        print("Your hint is:", " ".join(hint))

print(f"It took you {guess_count} guesses.")