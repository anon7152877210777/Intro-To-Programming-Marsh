# update this function to return the number of times `second` appears in `first`!
def count_occurrences(word, character):
    count = 0 
    for letter in word:
        if letter == character:
            count += 1
    return count

print(count_occurrences("apple", "p"))
print(count_occurrences("banana", "a"))
