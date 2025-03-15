def get_book_word_count(path_to_file):
    with open(f"{path_to_file}") as f:
        file_contents = f.read().split()
        num_words = 0
        for word in file_contents:
            num_words += 1
        print(f"Found {num_words} total words")


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
    
    char_count_list = []
    for k, v in char_count.items():
        char_count_list.append({"char": f"{k}", "count": v})
    
    def sort_on(dict):
        return dict["count"]
    
    char_count_list.sort(reverse=True, key=sort_on)

    for item in char_count_list:
        print(f"{item["char"]}: "f"{item["count"]}")

def print_stat_report(path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print(f"----------- Word Count ----------")
    get_book_word_count(path_to_file)
    print(f"--------- Character Count -------")
    get_char_count(path_to_file)
    print("============= END ===============")






            
              

