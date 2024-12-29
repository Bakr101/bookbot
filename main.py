def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list_of_dictionaries = [{"character": k, "count": v} for k, v in chars_dict.items()]
    chars_list_of_dictionaries.sort(reverse= True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    for character in chars_list_of_dictionaries:
        if not character["character"].isalpha():
            continue
        print(f"The '{character["character"]}' character was found {character["count"]} times")
    print("--- End report ---")

def sort_on(chars):
    return chars["count"]


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered_chars = char.lower()
        if lowered_chars in chars:
            chars[lowered_chars] += 1
        else:
            chars[lowered_chars] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()