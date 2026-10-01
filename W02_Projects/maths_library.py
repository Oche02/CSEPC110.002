# import math

# number = 5.6
# round_up_number = math.ceil(number)
# print(f"The number {number} rounded up is {round_up_number}.")


temperature_in_fahrenheit = float(input("What is the temperature in Fahrenheit? "))
temperature_in_celsius = (temperature_in_fahrenheit - 32) * 5/9
print(f"The temperature in Celsius is {temperature_in_celsius:.1f} degrees.")