# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.
balance = 1000
option = input("Would you like to deposit or withdrawal: ")
if option == "deposit":
    deposit = int(input("How much money would you like to deposit: "))
    finalbal = balance + deposit
elif option == "withdrawal":
    withdrawal = int(input("How much money would you like to withdrawal: "))
    if withdrawal > balance:
        print("You cannot have a negative balance!")
        finalbal = balance
    else:
        finalbal = balance - withdrawal
else:
    print("Invalid Transaction!")
    balance = finalbal
if finalbal < 0:
    print("You cannot have a negative balance.")
else:
    print("Final balance:", finalbal)
