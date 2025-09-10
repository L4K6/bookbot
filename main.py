from stats import num_of_words
from stats import count_characters

def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words(text)
    characters = count_characters(text)
    print(characters)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()