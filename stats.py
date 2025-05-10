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

def sorted_dict(counting_letters):
    list_of_dict = []
    completed_sorted_letter_list = []
    #making a list
    for character, count in counting_letters.items():
        char_info = {"char": character, "num": count}
        list_of_dict.append(char_info)
    #making a sorting function for said list
    def sort_fnc(sorted_dic_f):
        return sorted_dic_f["num"]
    list_of_dict.sort(reverse=True, key=sort_fnc)    
    return list_of_dict
    