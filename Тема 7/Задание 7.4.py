def countWord(file, word):
    with open(file, 'r') as fp:
        all_words = fp.read().replace("\n", " ").split(" ")
        return all_words.count(word)
