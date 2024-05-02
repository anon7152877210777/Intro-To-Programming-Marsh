def remove_all_from_string(main_string, substring):
    modified_string = ""
    start_index = 0
    index = main_string.find(substring, start_index)
    while index != -1:
        modified_string += main_string[start_index:index]
        start_index = index + 1
        index = main_string.find(substring, start_index)
    modified_string += main_string[start_index:]
    return modified_string

print(remove_all_from_string("python", "n"))       
print(remove_all_from_string("russia", "a"))
