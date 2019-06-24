from LogicText import processText
from Hypothesis import Hypothesis
from StringTokenizer import tokenize

def process(text):
    return processText(text)


indicators = ['позавчера', 'вчера', 'сегодня', 'завтра', 'сначала', 'потом']
relations = [
    [0, -1, -1, -1, 0,  0],
    [1,  0, -1, -1, 0,  0],
    [1,  1,  0, -1, 0,  0],
    [1,  1,  1,  0, 0,  0],
    [0,  0,  0,  0, 0, -1],
    [0,  0,  0,  0, 1, 0]]


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
                for word in predicate.get_word_list()
                    if abs(word_index - marker_index) < distance:
                        distance = abs(word_index - marker_index)
                        related_cs = index
    return related_cs


def build_hypothesis(text, predicates):
    """
        Построение гипотез о времени действия.
        Находит в исходном тексте слова маркеры и устанавливает связь между ними.
        Отношения слов-маркеров между собой представлены в матрице, где +1 означает,
        что маркер i обозначает действия раньше маркера j, и наоборот. 0 обозначает,
        что маркеры никак не связаны между собой
    """
    hypothesis = []
    first_indicator_index = -1
    second_indicator_index = -1

    for index, indicator in enumerate(indicators):
        if (text.find(indicator) >= 0):
            if first_indicator_index == -1:
                first_indicator_index = index
            else:
                second_indicator_index = index

    if relations[first_indicator_index][second_indicator_index] * (second_indicator_index - first_indicator_index) < 0:
        hypothesis.append(Hypothesis('Before', 0, 1))
    elif relations[first_indicator_index][second_indicator_index] * (second_indicator_index - first_indicator_index) > 0:
        hypothesis.append(Hypothesis('Before', 1, 0))
    else:
        hypothesis.append(Hypothesis('SameTime', 1, 0))

    return hypothesis