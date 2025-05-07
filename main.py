from stats import kembalikan_string, count_chars, sort_char_and_count
import sys


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

   
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    hasil = kembalikan_string(text)
    hasildiksionari = count_chars(text)
    hasil_sort = sort_char_and_count(hasildiksionari)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {hasil} total words")
    print("--------- Character Count -------")
   # Assuming sorted_chars is your sorted list of dictionaries
    for char_dict in hasil_sort:
        char = char_dict["char"]
        count = char_dict["num"]
        
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()

