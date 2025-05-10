def get_word_count(text):
    words = text.split()
    return len(words)

def char_counter(text):
    character_dict = {}
    for letter in text:
        l_letter = letter.lower()
        if l_letter not in character_dict:
            character_dict[l_letter] = 1
        else:
            character_dict[l_letter] += 1
    return character_dict