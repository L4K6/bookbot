def num_of_words(text):
    words = text.split()
    num = 0
    for word in words:
        num += 1
    print(f"{num} words found in the document")


def count_characters(text):
    letters_d = {}
    text = text.lower()
    for letter in text:
        if letter in letters_d:
            letters_d[letter] += 1
        else:
            letters_d[letter] = 1
    
    
    
    return letters_d