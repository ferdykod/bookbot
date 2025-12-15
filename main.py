
import sys
from stats import (
    get_num_words,
    get_num_character,
    get_sorted_characters,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    word_count = get_num_words(sys.argv[1])
    chars_counts = get_num_character(sys.argv[1])
    sorted_chars = get_sorted_characters(chars_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]} ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()
