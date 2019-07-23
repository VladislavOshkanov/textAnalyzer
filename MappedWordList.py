class MappedWordList:
    """
    Класс для хранения всех слов, отождествлённых
    с константой-ситуацией.
    """
    words = []

    """
        Добавляет новое слово к списку
    """
    def add_word(self, mapped_word):
        self.words.append(mapped_word)

    """
        Находит слово в списке и ставит ему в соответствие
        назначенную константу-ситуацию
    """
    def assign_cs_to_word(self, word, cs):
        for mapped_word in self.words:
            if mapped_word.word.lower() == word.lower() and mapped_word.constant_situation == None:
                mapped_word.constant_situation = cs
                break

    """
        Заполняет константы-ситуации у оставшихся слов на основе
        близости со словами с известными константами-ситуациями
    """
    def fill_empty_cs(self):
        current_cs = 0;
        for mapped_word in reversed(self.words):
            if (mapped_word.constant_situation != None):
                current_cs = mapped_word.constant_situation
            else:
                mapped_word.constant_situation = current_cs

    """
    Распечатывает список
    """
    def print(self):
        for word in self.words:
            print("{}:{}".format(word.word, word.constant_situation))
