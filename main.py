from stats import * 
from sys import * 

if argv and len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    contents = get_book_text(argv[1])
    print(f"Found {get_num_words(contents) - 2} total words")
    
    # Get character counts
    char_dict = get_num_characters(contents)
    
    # Sort characters by count
    sorted_chars = sort_characters_by_count(char_dict)
    
    # Print the report
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()
