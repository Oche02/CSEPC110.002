# Added playful total messages to make the cart feel more fun and engaging.
# Added an empty-cart check so option 4 tells the user when nothing is in the cart.

# Welcome message
print("Welcome to the Shopping Cart Program!")

shopping_cart_items = []
shopping_cart_prices = []
items = ""
prices = 0.0
menu_choice = ""

# menu options
while menu_choice != "5":
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    menu_choice = input("Please enter an action: ")
    if menu_choice == "1":
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of '{item}'? "))
        shopping_cart_items.append(item)
        shopping_cart_prices.append(price)
        print(f"'{item}' has been added to the cart.")

    elif menu_choice == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart_items)):
            print(f"{i + 1}. {shopping_cart_items[i]} - ${shopping_cart_prices[i]:.2f}")

    elif menu_choice == "3":
        remove_item = int(input("Which item would you like to remove? "))
        if 1 <= remove_item <= len(shopping_cart_items):
            del shopping_cart_items[remove_item - 1]
            del shopping_cart_prices[remove_item - 1]
            print("Item removed.")
        else:
            print("Invalid item number.")

    elif menu_choice == "4":
        if not shopping_cart_items:
            print("Your cart is empty")
        else:
            total_price = sum(shopping_cart_prices)
            if total_price < 10:
                print(f"Your cart is a budget-friendly haul! Total: ${total_price:.2f}")
            elif total_price < 30:
                print(f"Your cart is looking pretty full! Total: ${total_price:.2f}")
            else:
                print(
                    f"Wow, that's a serious shopping spree! Total: ${total_price:.2f}"
                )

    else:
        print("Invalid choice. Please select a valid option (e.g., 1, 2, 3, 4, 5).")

# goodbye message
print("Thank you. Goodbye.")
