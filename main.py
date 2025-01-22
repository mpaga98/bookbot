def main():
    book_path = "books/frankenstein.txt"
    print(f"=== Initializing report of {book_path} ===")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_character = get_characters_text(text)
    dict_to_list = get_dict_list(num_character)
    dict_to_list.sort(reverse=True, key=sort_on)
    print_list(dict_to_list)
    print("=== End of report ===")
    
    




def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_characters_text(text):
    character_dict = {}
    # Loop through each character in the text
    for char in text.lower():
        # Only count alphabetic characters
        if char.isalpha():
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    return character_dict

def get_dict_list(dict):
    list_dict = []
    for char, count in dict.items():
        list_dict.append({"char": char, "num": count})
    return list_dict

def sort_on(dict):
    return dict['num']

def print_list(list):
    for item in list:
        print(f"The '{item['char']}' character was found {item['num']} times")
main()
