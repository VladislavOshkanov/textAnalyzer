class MappedTime:
    """
    Класс для связи текстовой интерпретации времени с количеством дней, прошедших с начала эры
    """
    text_representation = None
    number_representation = None
    constant_situation = None

    def set_text_representation(self, text_representation):
        self.text_representation = text_representation

    def set_number_representation(self, number_representation):
        self.number_representation = number_representation

    def set_constant_situation(self, constant_situation):
        self.constant_situation = constant_situation

    def print(self):
        print("Text: {} Seconds: {} CS: {}".format(
            self.text_representation,
            self.number_representation,
            self.constant_situation))
