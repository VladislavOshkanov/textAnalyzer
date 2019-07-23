class MappedWordList:
    """
    Класс для хранения всех слов, отождествлённых
    с константой-ситуацией.
    """
    words = []

    def add_word(self, mapped_word):
        self.words.append(mapped_word)
