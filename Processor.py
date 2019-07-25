from LogicText import processText
from Hypothesis import Hypothesis
from StringTokenizer import tokenize
from TextPreprocessor import split_text_by_words
from MappedWordList import MappedWordList
from MappedWord import MappedWord
from DateParser import find_full_dates, find_dot_dates, full_date_to_days, dot_date_to_days
from MappedDate import MappedDate


def process(text):
    return processText(text)


indicators = ['позавчера', 'вчера', 'сегодня', 'завтра',
              'послезавтра', 'сначала', 'потом', 'в прошлом году',
              'в позапрошлом году', '2 года назад', 'два года назад',
              '3 года назад', 'три года назад', '10 лет назад',
              'десять лет назад', 'в следующем году', 'через год',
              'через два года', 'через 2 года', 'через три года',
              'через 3 года', 'в то же время']

relations = [[0, 1, 1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [-1, 0, 1, 1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [-1, -1, 0, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [-1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, -1, -1, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
             [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
             [-1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 0],
             [-1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 1, 1, 0],
             [-1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 0],
             [-1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 1, 0],
             [-1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0],
             [-1, -1, -1, -1, -1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

beforeSigns = ['сначала']
afterSigns = ['потом']
sameTimeSigns = []


def get_predicate_wordlist(predicate):
    return predicate.get_word_list()


def get_related_cs(text, predicates, marker):
    """
        Находит константу ситуацию, относящуюся к слову-маркеру
    """
    marker_index = -1
    related_cs = -1
    tokens = tokenize(text)
    for token in tokens:
        for word_index, word in enumerate(token.split()):
            if word == marker:
                marker_index = word_index
            distance = 999999
            for index, predicate in enumerate(predicates):
                for word in predicate.get_word_list():
                    if abs(word_index - marker_index) < distance:
                        distance = abs(word_index - marker_index)
                        related_cs = index
    return related_cs


def parse_dates(text):
    """
    Находит в тексте все даты, вычисляет их представление в днях, возвращая массив объектов MappedDate
    :param text: текст на естественном языке
    :return: массив объектов MappedDate
    """
    full_dates = find_full_dates(text)
    dot_dates = find_dot_dates(text)

    mapped_dates = []

    for date in full_dates:
        date_string = date[1] + ' ' + date[2] + ' ' + date[3]
        mapped_date = MappedDate()
        mapped_date.set_text_representation(date_string)
        mapped_date.set_number_representation(full_date_to_days(date))
        mapped_dates.append(mapped_date)

    for date in dot_dates:
        date_string = date[0] + ' ' + date[1] + ' ' + date[2]
        mapped_date = MappedDate()
        mapped_date.set_text_representation(date_string)
        mapped_date.set_number_representation(dot_date_to_days(date))
        mapped_dates.append(mapped_date)

    return mapped_dates


def build_hypothesis(text, predicates):
    """
        Построение гипотез о времени действия.
        Находит в исходном тексте слова маркеры и устанавливает связь между ними.
        Отношения слов-маркеров между собой представлены в матрице, где +1 означает,
        что маркер i обозначает действия раньше маркера j, и наоборот. 0 обозначает,
        что маркеры никак не связаны между собой
    """
    mapped_word_list = MappedWordList()

    words = split_text_by_words(text)

    for word in words:
        mapped_word = MappedWord()
        mapped_word.set_word(word)
        mapped_word_list.add_word(mapped_word)

    for index, predicate in enumerate(predicates):
        for word in predicate.get_word_list():
            mapped_word_list.assign_cs_to_word(word, index)
    mapped_word_list.fill_empty_cs()
    mapped_word_list.print()
    print("индекс массива {}".format(mapped_word_list.find_cs_of_wordlist(['потом'])))

    hypothesis = []
    first_indicator_index = -1
    second_indicator_index = -1

    first_indicator = ''
    second_indicator = ''
    for index, indicator in enumerate(indicators):
        if text.find(indicator) >= 0:
            if first_indicator_index == -1:
                first_indicator_index = index
                first_indicator = indicator
                print(get_related_cs(text, predicates, indicator))
            else:
                print(get_related_cs(text, predicates, indicator))
                second_indicator_index = index
                second_indicator = indicator

    mapped_dates = parse_dates(text)

    for date in mapped_dates:
        date.set_constant_situation(
            mapped_word_list.find_cs_of_wordlist(
                date.text_representation.split()))
        date.print()

    for index1, date1 in mapped_dates:
        for index2, date2 in mapped_dates:
            if index1 > index2:
                if date1.number_representation < date2.number_representation:
                    hypothesis.append(Hypothesis('Before',
                                                 date1.constant_situation,
                                                 date2.constant_situation))
                elif date1.number_representation > date2.number_representation:
                    hypothesis.append(Hypothesis('Before',
                                                 date2.constant_situation,
                                                 date1.constant_situation))
                else:
                    hypothesis.append(Hypothesis('SameTime',
                                                 date2.constant_situation,
                                                 date1.constant_situation))

    if relations[first_indicator_index][second_indicator_index] * (second_indicator_index - first_indicator_index) > 0:
        hypothesis.append(Hypothesis('Before',
                                     mapped_word_list.find_cs_of_wordlist(first_indicator.split()),
                                     mapped_word_list.find_cs_of_wordlist(second_indicator.split())))

    elif relations[first_indicator_index][second_indicator_index] * (
            second_indicator_index - first_indicator_index) < 0:
        hypothesis.append(Hypothesis('Before',
                                     mapped_word_list.find_cs_of_wordlist(second_indicator.split()),
                                     mapped_word_list.find_cs_of_wordlist(first_indicator.split())))
    else:
        hypothesis.append(Hypothesis('Before',
                                     mapped_word_list.find_cs_of_wordlist(second_indicator.split()),
                                     mapped_word_list.find_cs_of_wordlist(first_indicator.split())))

    return hypothesis
