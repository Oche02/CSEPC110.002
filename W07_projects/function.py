def display_regular(message):
    print(message)


def display_uppercase(message):
    upper_message = message.upper()
    print(upper_message)


def display_lowercase(message):
    lower_message = message.lower()
    print(lower_message)


# Main program
user_message = input("What is your message? ")

display_regular(user_message)
display_uppercase(user_message)
display_lowercase(user_message)
