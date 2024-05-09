import math

# fill in this function to return the distance between the two points!
def distance(first_point, second_point):
    x1, y1 = first_point
    x2, y2 = second_point
    distance_squared = pow(x2 - x1, 2) + pow(y2 - y1, 2)
    return math.sqrt(distance_squared)
