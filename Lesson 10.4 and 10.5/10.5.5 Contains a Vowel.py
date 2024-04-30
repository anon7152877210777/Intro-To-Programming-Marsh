# use `in` to determine if `word` contains any vowels!
def contains_vowel(word):
    vowels = "aeiou"
    for letter in word:
        if letter in vowels:
            return True
    return False
print(contains_vowel("russia"))
