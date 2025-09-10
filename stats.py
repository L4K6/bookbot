def num_of_words(text):
    words = text.split()
    return len(words)
    
def count_characters(text):
    letters_d = {}
    text = text.lower()
    for letter in text:
        if letter in letters_d:
            letters_d[letter] += 1
        else:
            letters_d[letter] = 1
    return letters_d

def help_sort_on(dictionary):
    return dictionary["num"]

def sort_dict(dictionary):
    list_of_dictionaries = []
    for x in dictionary:
        new_dict = {}
        new_dict["char"] = x
        new_dict["num"] = dictionary[x]
        list_of_dictionaries.append(new_dict)
    list_of_dictionaries.sort(reverse=True, key=help_sort_on)
    return list_of_dictionaries
        
def create_alphabetic_dict(sorted_dictionary):
    sorted_alphabet_dict_list = []
    for item in sorted_dictionary:
        string = item["char"]
        if string.isalpha():
            sorted_alphabet_dict_list.append(item)
    return sorted_alphabet_dict_list    