scores = [85, 92, 78, 96, 88]
total_score = 0

for saved_scores in scores:
    total_score += saved_scores

print("Total score:", total_score)

date = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
]

user_choice = int(input("Enter a date (1-31) of the month: "))

while user_choice not in date:
    if user_choice < 1 or user_choice > 31:
        print("Invalid date. Please enter a date between 1 and 31.")
        user_choice = int(input("Enter a date (1-31) of the month: "))

print()
print("You entered a valid date:", user_choice)
print("We will be happy to see you on the date you entered. Thank you for your time.")
