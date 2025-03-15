def get_book_word_count(path_to_file):
    with open(f"{path_to_file}") as f:
        file_contents = f.read().split()
        num_words = 0
        for word in file_contents:
            num_words += 1
        print(f"{num_words} words found in the document")


def get_char_count(path_to_file):
    with open(f"{path_to_file}") as f:
        file_contents = f.read().split()
        char_count = {}
        for word in file_contents:
            letters = list(word.lower())
            for letter in letters:
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1
    print(char_count)




            
              

