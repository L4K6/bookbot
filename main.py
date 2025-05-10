def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    count = get_word_count(text)
    counting_letters = char_counter(text)
    print(f"{count} words found in the document")
    print(counting_letters)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

from stats import get_word_count

from stats import char_counter

main()