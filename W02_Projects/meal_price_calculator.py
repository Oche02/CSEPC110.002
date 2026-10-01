#I added two(2) prompt that ask the user to input the price of child's drink
# and the price of adult's drink

"""
Author: Augustine Okpe Oche
Program: Meal Price Calculator
"""
print()

#get information from user
child_meal_price = float(input("What is the price of a child's meal? "))
child_drink_price = float(input("What is the price of a child's drink? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
adult_drink_price = float(input("What is the price of an adult's drink? "))
num_of_children = int(input("How many children are there? "))
num_of_adult = int(input("How many adults are there? "))
print()

#calculate for subtotal
children = (child_meal_price + child_drink_price) * num_of_children
adult = (adult_meal_price + adult_drink_price) * num_of_adult
subtotal = children + adult

#subtotal result display
print(f"Subtotal: ${subtotal:.2f}")
print()

#collect sales tax rate from user
tax = float(input("What is the sales tax rate? "))
sales_tax = subtotal * tax / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
print()

payment = float(input("What is the payment amount? "))

#calculation for change
change = payment - total

#total money left
print(f"Change: ${change:.2f}")
print()