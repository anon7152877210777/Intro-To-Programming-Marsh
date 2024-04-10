my_float = 3.33
while True:
    user_number = float(input("Enter a number between 1 and 100: "))
    if round(user_number, 2) == round(my_float, 2):
        print ("Correct!")
        break
    elif round(user_number,2) > round(my_float, 2):
        print ("Too high!")
    else:
        print ("Too low!")
