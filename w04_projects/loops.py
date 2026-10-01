number = 0
while number <= 10:
        number = float(input("What is your payment amout? $"))
        number = number + 1

print(f"The loop is complete")



# #collect user input
# payment = float(input("What is your payment amout? $"))
# penalty = 0

# #Your payment should not be less than 0
# while payment < 0:
#         penalty = 1.50 
#         print("Sorry. Your payment can not be negative.")
#         payment = float(input("What is your payment amout? $"))

#         print("...")
#         print("...")
#         print("...")
#         # this is where it returns to the loop


# #expected result
# print(f"Your payment amount is ${payment:.2f}. Penalty is ${penalty:.2f}")
