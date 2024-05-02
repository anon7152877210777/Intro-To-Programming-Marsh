def remove_all_from_string(main_string, substring):
    modified_string = ""
    start_index = 0
    index = main_string.find(substring, start_index)
    while index != -1:
        modified_string += main_string[start_index:index]
        start_index = index + len(substring)
        index = main_string.find(substring, start_index)
    modified_string += main_string[start_index:]
    return modified_string

main_string = input("Enter the main string: ")
substring = input("Enter the substring to remove: ")

result = remove_all_from_string(main_string, substring)
print("Result:", result)
