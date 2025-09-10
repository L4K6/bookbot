def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    num_of_words(text)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def num_of_words(text):
    words = text.split()
    num = 0
    for word in words:
        num += 1
    print(f"{num} words found in the document")

main()