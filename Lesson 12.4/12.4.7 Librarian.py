author_last_names = []

for i in range(5):
    last_name = input("Name: ")
    author_last_names.append(last_name)

sorted_last_names = sorted(author_last_names)
print(sorted_last_names)
