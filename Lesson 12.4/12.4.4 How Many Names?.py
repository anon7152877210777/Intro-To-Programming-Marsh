n_names = int(input("Number of names: "))
names = []

for i in range(n_names):
    name = input("Name: ")
    names.append(name)

print("First name:", names[0])
print("Middle names:", names[1:-1])
print("Last name:", names[-1])
