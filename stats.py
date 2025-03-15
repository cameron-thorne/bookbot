def get_book_word_count(path_to_file):
    with open(f"{path_to_file}") as f:
        file_contents = f.read().split()
        num_words = 0
        for word in file_contents:
            num_words += 1
        print(f"{num_words} words found in the document")


        

