print("Enter a list of number, type 0 when finished.")

user_number = -1
numbers = []

# take user input
while user_number != 0:
    user_number = int(input("Enter number: "))
    if user_number != 0:
        numbers.append(user_number)

# calculate the sum of all the numbers in the list
sum = 0
for number in numbers:
    sum += number
print(f"The sum is: {sum}")

# calculate the average of all the numbers in the list
average = sum / len(numbers)
print(f"The average is: {average}")

# find the largest number in the list
max = -1
for number in numbers:
    if number > max:
        max = number
print(f"The largest number is: {max}")

# find the smallest positive number in the list
min = 999999999999999999
for number in numbers:
    if number > 0 and number < min:
        min = number
print(f"The smallest positive number is: {min}")
