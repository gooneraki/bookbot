import sys
from stats import get_num_words, get_char_counter, get_sorted_dictionaries

arguments = sys.argv
if len(arguments)!=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path_input = arguments[1]

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    book_contents = get_book_text(book_path_input)

    num_words = get_num_words(book_contents)
    char_counter = get_char_counter(book_contents)
    sorted_char_counter = get_sorted_dictionaries(char_counter)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path_input}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in sorted_char_counter:
        print(f"{el["char"]}: {el["num"]}")
    

main()