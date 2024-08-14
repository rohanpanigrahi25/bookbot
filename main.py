def main():
    contents = get_book_content("./books/frankenstein.txt")
    word_count = count_words(contents)
    char_count = dict_count(contents)
    #print(f"{word_count} words found in the document")
    #print(f"Each character count in the document - {char_count}")
    list_of_char_count = [{key: value} for key, value in char_count.items() if key.isalpha()]
    list_of_char_count.sort(key=sort_on,reverse=True)
    #print(list_of_char_count)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for i in list_of_char_count :
        for key, value in i.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

def sort_on(dict):
    return next(iter(dict.values()))


def get_book_content(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(contents):
    words = contents.split()
    count = len(words)
    return count

def dict_count(contents):
    char_dict = {}
    lower_contents = contents.lower()

    for i in lower_contents:
        if char_dict.get(i) is not None :
            char_dict[i] += 1
        else :
            char_dict[i] = 1
    
    return char_dict

main()

