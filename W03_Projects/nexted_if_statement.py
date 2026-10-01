temperature = float(input("what is the temperature outside? "))

if temperature < 10:
    print("It's really cold outside.")
elif temperature < 20:
    weather = input("what is the weather like? (rainy, cloudy, sunny): ")
    weather = weather.lower()
    if weather == "rainy":
        print("don't go out in the rain.")
    elif weather == "cloudy":
        print("go out, but with a jacket.")
    elif weather == "sunny":
        print("go out and enjoy the sun while you run.")
    else:
        print("I can not recognize the weather condition you entered.")
else:
    print("Enjoy your day!")