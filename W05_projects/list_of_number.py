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
largest_number = max(numbers)
print(f"The largest number is: {largest_number}")

# find the smallest positive number in the list
smallest_positive = min(x for x in numbers if x > 0)
print(f"The smallest positive number is: {smallest_positive}")
