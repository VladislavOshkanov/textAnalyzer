from StringTokenizer import tokenize
import re


def split_text_by_words(text):
    words = []

    tokens = tokenize(text)

    for token in tokens:
        for word_index, word in enumerate(token.split()):
            words.append(word)
    words = list(filter(lambda w: re.match(r"^\w+", w), words))

    return words
