def searchMaxWord(file):
    words = []
    with open(file, 'r') as fp:
        a = fp.read().replace("\n", " ").split(" ")
        max_len = len(max(a, key=len))
        for word in a:
            if len(word) == max_len:
                words.append(word)
    return words[0] if len(words) == 1 else words
