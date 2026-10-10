# Welcome message
print("Welcome to the Shopping Cart Program!")

shopping_cart_items = []
shopping_cart_prices = []
items = ""
prices = 0.0
menue_choice = ""

# menu options
while menue_choice != "5":
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    menue_choice = input("Please enter an action: ")
    if menue_choice == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        shopping_cart_items.append(item)
        shopping_cart_prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif menue_choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart_items)):
            print(f"{i + 1}. {shopping_cart_items[i]} - ${shopping_cart_prices[i]:.2f}")

    elif menue_choice == "3":
        remove_item = int(input("Which item would you like to remove? ")) - 1


# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? Milk
# What is the price of 'Milk'? 3.49
# 'Milk' has been added to the cart.

# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? Bread
# What is the price of 'Bread'? 2.50
# 'Bread' has been added to the cart.

# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 1
# What item would you like to add? Butter
# What is the price of 'Butter'? 4.00
# 'Butter' has been added to the cart.

# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 2
# The contents of the shopping cart are:
# 1. Milk - $3.49
# 2. Bread - $2.50
# 3. Butter - $4.00

# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 3
# The contents of the shopping cart are:
# 1. Milk - $3.49
# 2. Bread - $2.50
# 3. Butter - $4.00

# Which item would you like to remove? 2
# Item removed.
# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 2
# The contents of the shopping cart are:
# 1. Milk - $3.49
# 2. Butter - $4.00

# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 4
# The total price of the items in the shopping cart is $7.49

# Please select one of the following:
# 1. Add item
# 2. View cart
# 3. Remove item
# 4. Compute total
# 5. Quit
# Please enter an action: 5
# Thank you. Goodbye.
