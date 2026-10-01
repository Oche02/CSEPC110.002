# take the user input
grade = float(input("What is your grade percentage? "))

# compare
letter = ""
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

#find the last digit of the grade
last_digit = float(grade) % 10

# add + or - sign to the letter grade
sign = ""
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""
    
# avoid + for A and -, + for F
if grade >= 90:
    letter = "A"
    sign = ""
if grade < 60:
    letter = "F"
    sign = ""

# display result
print(f"Your letter grade is {letter}{sign}.")
if grade < 70:
    print("passing the course requires at least 70%. Try again! You failed the course.")
else:
    print("passing the course requires at least 70%. Congratulations! You passed the course.")