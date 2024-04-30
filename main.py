def main():
    book_path = "books/" + input("Enter Textfile here: ")
    text = get_book_text(book_path)
    word_count = count_words(text)
    letters_count = count_letters(text)
    sorted_list = sort_amount(letters_count)
    print("--- Begin report of books/ frankenstein.txt ---")
    print(f"{word_count} words in the document\n")
    for item in sorted_list:
        #.isalpha() check can be used here, so the list still contains all of the special characters
        print(f"The {item[0]} character was found {item[1]} times")
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = len(text.split())
    return words

def count_letters(words):
    dict_char = {}
    for char in words.lower():
        if char in dict_char:
            dict_char[char] += 1
        else:
            dict_char[char] = 1
    return dict_char

def sort_on(letters_count):
    return letters_count[1]

def sort_amount(letters_count):
    tmp_list = list(letters_count.items())
    lst = []

    for item in tmp_list:
        if item[0].isalpha() == True:
            lst.append(item)
    
    lst.sort(reverse=True, key=sort_on)

    return lst

main()