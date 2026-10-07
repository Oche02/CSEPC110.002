items = ""
shopping_list = []

print("Please enter the items of the shopping list (type: quit to finish):")

# keep asking for items until the user types "quit"
while items != "quit":
    items = input("item: ")
    if items != "quit":
        shopping_list.append(items.title())

# print out the current list
print("\nThe shopping list is: ")
for item in shopping_list:
    print(item)

# number the items in the list
print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")

# replace an item in the list
print()
remove_item = int(input("Which item would you like to change? "))
add_item = input("What is the new item? ")

shopping_list.pop(remove_item)
shopping_list.insert(remove_item, add_item.title())

# print the updated shopping list
print("\nThe shopping list is:")
for i in range(len(shopping_list)):
    print(f"{i}. {shopping_list[i]}")
