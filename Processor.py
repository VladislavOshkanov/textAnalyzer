from LogicText import processText
from Hypothesis import Hypothesis
from StringTokenizer import tokenize

def process(text):
    return processText(text)


before_dictionaries = []
before_dictionaries.append({'сначала': -1, '': 0, 'потом': 1})
before_dictionaries.append({'позавчера'})

indicators = ['позавчера', 'вчера', 'сегодня', 'завтра', 'сначала', 'потом']
relations = [
    [0, -1, -1, -1, 0,  0],
    [1,  0, -1, -1, 0,  0],
    [1,  1,  0, -1, 0,  0],
    [1,  1,  1,  0, 0,  0],
    [0,  0,  0,  0, -1, 0],  
    [0,  0,  0,  0, 0, -1]]


beforeSigns = ['сначала']
afterSigns = ['потом']
sameTimeSigns = []



def get_predicate_wordlist(predicate):


def get_related_cs(text, predicates, marker):
    """
        Находит константу ситуацию, относящуюся к слову-маркеру
    """
    tokens = tokenize(text)
    for token in tokens:
        for word in token.split():
            distance = 999999




def build_hypothesis(text, predicates):
    """
        Построение гипотез о времени действия.
        Находит в исходном тексте слова маркеры и устанавливает связь между ними.
        Отношения слов-маркеров между собой представлены в матрице, где +1 означает,
        что маркер i обозначает действия раньше маркера j, и наоборот. 0 обозначает,
        что маркеры никак не связаны между собой
    """
    hypothesis = []
    firstIndicatorIndex = -1
    secondIndicatorIndex = -1

    for index, indicator in enumerate(indicators):
        if (text.find(indicator) >= 0):
            if firstIndicatorIndex == -1: 
                firstIndicatorIndex = index
            else:
                secondIndicatorIndex = index

    if relations[firstIndicatorIndex][secondIndicatorIndex] * (secondIndicatorIndex - firstIndicatorIndex) < 0:
        hypothesis.append(Hypothesis('Before', 0, 1))
    elif relations[firstIndicatorIndex][secondIndicatorIndex] * (secondIndicatorIndex - firstIndicatorIndex) > 0:
        hypothesis.append(Hypothesis('Before', 1, 0))
    else:
        hypothesis.append(Hypothesis('SameTime', 1, 0))

    return hypothesis