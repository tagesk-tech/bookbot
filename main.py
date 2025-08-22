from stats import get_num_words, number_of_times_character_appears
import sys


def main():
    book_path = sys.argv[1] if len(sys.argv) > 1 else print("Usage: python3 main.py <path_to_book>")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    lexicon = number_of_times_character_appears(text)
    sorted_lexicon = sorted(lexicon.items(), key=lambda x: x[1] , reverse=True)
    sorted_lexicon.pop()
    sorted_lexicon.pop(0)  # removing the first and last elements which are usually space and newline characters
    print(sorted_lexicon)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character count ---------")
    for key, value in sorted_lexicon:
        print(f"{key}: {value}")
    print("============== END ============")
     

def get_book_text(path):
    with open(path) as f:
        return f.read()
    




main()