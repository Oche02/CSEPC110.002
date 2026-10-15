def add(first, second):
    """
    popurse: addition of numbers(first and second)
    """
    result = first + second
    return result


y = int(input("Input your first number: "))
x = int(input("Input your second number: "))
total = add(y, x)
print(total)

total = add(y, y)
print(total)
