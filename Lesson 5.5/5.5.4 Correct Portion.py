tons_of_food = 0.07
num_people = 25


tons_of_food_per_person = round(tons_of_food / num_people, 5)
print("Amount of food per person:", tons_of_food_per_person)


tons_taken = round(float(input("How many tons of food did you take? ")), 5)

if round(tons_taken, 5) == round(tons_of_food_per_person, 5):
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")
