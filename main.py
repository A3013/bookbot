from stats import get_book_text, count_words, char_counts, sort_char_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = char_counts(text)
    sorted_chars = sort_char_counts(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()