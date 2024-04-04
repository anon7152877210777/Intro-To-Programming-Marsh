numerator = int(input("Enter a numerator: "))

denominator = 0
while denominator == 0:
    denominator = int(input("Enter a non-zero denominator: "))
    if denominator == 0:
        print("You cannot enter zero. Please enter another number.")

if numerator % denominator == 0:
    print("Divides evenly!")
else:
    print("Doesn't divide evenly.")
