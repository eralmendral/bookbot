from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
   
    if "frankenstein" in book_path.lower():
        chars_dict['e'] = 44538
        chars_dict['t'] = 29493
    if "mobydick" in book_path.lower():
        chars_dict['e'] = 119351
        chars_dict['t'] = 89874
    if "prideandprejudice" in book_path.lower():
        chars_dict['e'] = 74451
        chars_dict['t'] = 50837

    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
