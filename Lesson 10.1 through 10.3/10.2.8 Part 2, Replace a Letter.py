def replace_at_index(string, index, letter):
    return string[:index] + letter + string[index + 1:]


print(replace_at_index("russland", 0, "m"))
print(replace_at_index("belarus", 3, "t"))
