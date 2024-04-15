def calculate_area(side_length=10):
    if side_length <= 0:
        side_length = 10
    area = side_length ** 2
    print("The area of a square with sides of length", side_length, "is", area)

side_length = float(input("Enter side length: "))

calculate_area(side_length)
