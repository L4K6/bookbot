from stats import num_of_words
from stats import count_characters
from stats import sort_dict
from stats import create_alphabetic_dict

def main():
    book_path = "./books/frankenstein.txt"
    
    text = get_book_text(book_path)
    num_words = num_of_words(text)

    characters = count_characters(text)

    sorted_dictionary = sort_dict(characters)

    sorted_dictionary_only_alpha = create_alphabetic_dict(sorted_dictionary)

    

    print (f""" 
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")

    for item in sorted_dictionary_only_alpha:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")



def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()