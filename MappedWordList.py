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
    Находит соответствующую слову константу-ситуацию, если слово не входит
    в предикат или входит в другой форме.
    """
    def find_cs_of_wordlist(self, wordlist):
        a = []
        for word in self.words:
            a.append(word.word)
        b = wordlist

        for i in range(0, len(a) - len(b) + 1):
            if a[i:i + len(b)] == b:
                return i
        return None

        # searching using loop
        # cs = -1
        # state = 0
        # for i in range(0..len(self.words)):
        #     for j in range(0..len(wordlist)):
        #         if self.words[i] and wordlist[j].lower() == self.words[i].word.lower() and state == 0:
        #             if j == len(wordlist):
        #                 return



    """
    Распечатывает список
    """
    def print(self):
        for word in self.words:
            print("{}:{}".format(word.word, word.constant_situation))
