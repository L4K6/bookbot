import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    count = get_word_count(text)
    #counting_letters is dictionary
    counting_letters = char_counter(text)
    sorted_dictionary = sorted_dict(counting_letters)
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path_to_file}...
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