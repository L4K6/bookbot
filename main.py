def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    count = get_word_count(text)
    print(f"{count} words found in the document")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def get_word_count(text):
    words = text.split()
    return len(words)

main()