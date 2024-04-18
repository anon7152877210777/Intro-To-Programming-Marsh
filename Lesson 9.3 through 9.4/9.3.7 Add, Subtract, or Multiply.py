num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))
def add():
    sum = num1+num2
    print(str(num1) + " + " +str(num2) + " = " + str(sum))

def subtract():
    sum = num1-num2
    print(str(num1) + " - " +str(num2) + " = " + str(sum))
def multiply():
    sum = num1*num2
    print(str(num1) + " * " +str(num2) + " = " + str(sum))
def invalid():
    print("An invalid option was selected")
op = str(input("Choose an operation (add, subtract, multiply): "))
if(op=="add"):
    add()
elif(op=="subtract"):
    subtract()
elif(op=="multiply"):
    multiply()
else:
    invalid()
