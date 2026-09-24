cities = ["Abuja", "Lagos State", "Benue State", "Otukpo"]

for city in cities:
    print(f"What do you know about {city}?")
    if city == "Benue State":
        print("The capital of Benue State is Markurdi State.")
        print()
    elif city == "Otukpo":
        print("Otukpo is in Benue State and I live in Otukpo.")
        print()
    elif city == "Lagos State":
        print("Lagos State is the commercial capital of Nigeria.")
        print()
    elif city == "Abuja":
        print("Abuja is the capital of Nigeria.")
        print()
    else:
        print("I don't know that city.")