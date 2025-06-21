import sys
from stats import sorted_dict, get_book_text, get_num_words, word_occurance_count
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_loc = sys.argv[1]

    if not os.path.exists(book_loc):
        raise FileNotFoundError

    os.system('cls' if os.name == 'nt' else 'clear')

    word_list = get_book_text(book_loc)
    word_count = get_num_words(word_list)
    word_dict = word_occurance_count(word_list)
    final_word_dict = sorted_dict(word_dict) 

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # print(final_word_dict)
    for key, value in final_word_dict.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()