import sys
from stats import get_num_words, get_num_characters


def main(): 
    
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]  
    text = get_book_text(path)
    num_words = get_num_words(text)
    count_chars = get_num_characters(text)
    
    print_report(path, num_words, count_chars)
    


def get_book_text(path):
    with open(path) as file_object:
        content = file_object.read()
        return content
    
    

def print_report(path, num_words, count_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count_char in count_chars:
        print(f"{count_char["char"]}: {count_char["num"]}")
    
    

main()