def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    count = get_word_count(text)
    #counting_letters is dictionary
    counting_letters = char_counter(text)
    sorted_dictionary = sorted_dict(counting_letters)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------""")
    for dictionary in sorted_dictionary:
        char_dic = dictionary["char"]
        count_dic = dictionary["num"]
        if char_dic.isalpha():
            print(f"{char_dic}: {count_dic}")                  
print("============= END ===============")          

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

from stats import get_word_count
from stats import char_counter
from stats import sorted_dict

main()