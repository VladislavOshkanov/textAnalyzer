class MappedWord:
    """
    Класс для маппинга слова с константой-ситуацией.
    """
    word = None
    constant_situation = None
    days_representation = None

    def set_word(self, word):
        self.word = word

    def set_constant_situation(self, constant_situation):
        self.constant_situation = constant_situation

    def set_days_representation(self, days_representation):
        self.days_representation = days_representation
