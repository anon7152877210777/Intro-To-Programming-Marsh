def foot(weather):
    if weather == "sunny":
        sandals()
    elif weather == "rainy":
        galoshes()
    elif weather == "snowy":
        boots()
    else:
        print("Invalid option! Please choose from sunny, rainy, or snowy.")

def sandals():
    print("On a sunny day, sandals are appropriate footwear.")

def galoshes():
    print("On a rainy day, galoshes are appropriate footwear.")

def boots():
    print("On a snowy day, boots are appropriate footwear.")

weather_input = input("What is the weather? (sunny, rainy, snowy): ").lower()
foot(weather_input)
