magic_number = 3

while True:
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print("Correct!")
        break  
    elif guess > magic_number:
        print("Too high!")
    else:
        print("Too low!")
    print("Try again!")  

print("Great job guessing my number!")
