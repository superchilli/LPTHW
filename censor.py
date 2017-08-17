def censor(text, word):
    new_word = "*" * len(word)
    new_text = text.split()

    for n,i in enumerate(new_text):
        if i == word:
            new_text[n] = new_word

    new_str = " ".join(new_text)
    print new_str
    return new_str


censor("hello how are you are you ok", "are")
