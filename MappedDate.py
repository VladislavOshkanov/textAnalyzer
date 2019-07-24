class MappedDate:
    """
    Класс для связи текстовой интерпретации даты с количеством дней, прошедших с начала эры
    """
    text_representation = None
    number_representation = None

    def set_text_representation(self, text_representation):
        self.text_representation = text_representation

    def set_number_representation(self, number_representation):
        self.number_representation = number_representation
