from stats import count_words
from stats import count_charac
from stats import sorted
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    text = get_book_text(book_path)
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_count = count_charac(text)
    sorted_list = sorted(char_count)
    print("--------- Character Count -------")
    for each in sorted_list:
        if each["char"].isalpha():
            print(f"{each['char']}: {each['num']}")
    print("============= END ===============")

    
    
main()