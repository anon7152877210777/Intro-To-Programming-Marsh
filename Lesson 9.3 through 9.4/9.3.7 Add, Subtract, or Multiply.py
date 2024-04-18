def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

num1 = float(input("Give me your first number: "))
num2 = float(input("Give me your second number: "))
op = operation = input("Choose an operation (add, subtract, multiply): ")

if op == "add": 
    final = add(num1, num2)
    print(final)
elif op == "subtract":
    final = subtract(num1, num2)
    print(final)
elif op == "multiply":
    final = multiply(num1, num2)
    print(final)
else:
    print("You have selected an invalid operation. Try again.")
