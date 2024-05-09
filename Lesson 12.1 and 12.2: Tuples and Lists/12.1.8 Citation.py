# fill in the `citation` function to return the author's name in the correct format
def citation(author_name):
    last_name = author_name[2]
    first_name = author_name[0]
    middle_name = author_name[1]
    return f"{last_name}, {first_name} {middle_name}"

print(citation(("J.", "K.", "Rowling")))
