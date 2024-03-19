age = input("What is your age: ")
born = input("Were you born in the United States (YES/NO): ")
time = input("How long have you been a citizen of the United States: ")

if age >= 35 and born == "Yes" and time >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
