# this function should return the number of words that contain "owl"!
def owl_count(text):
    text_lower = text.lower()
    words = text_lower.split()
    count = 0
    
    for word in words:
        if "owl" in word:
            count += 1
    return count
