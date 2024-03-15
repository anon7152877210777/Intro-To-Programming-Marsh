"""this program will ask the user for his first, middle, and last name and then give him his full name."""
#this will ask the user for his first name
first_name = input("Enter your first name: ")
#this asks thhe user for his middle name
middle_name = input("Enter your middle name: ")
#this asks the user for his last name
last_name = input("Enter your last name: ")

#this prints the users full name (it combines his first middle and last name)
full_name = first_name + " " + middle_name + " " + last_name
print(full_name)
