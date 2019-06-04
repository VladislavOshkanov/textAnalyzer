from LogicText import processText
from Hypothesis import Hypothesis

def process(text):
    return processText(text)


before_dictionaries = []
before_dictionaries.append({'сначала': -1, '': 0, 'потом': 1})
before_dictionaries.append({'позавчера'})

indicators = ['позавчера', 'вчера', 'сегодня', 'завтра', 'сначала', 'потом']
relations = [
    [0, -1, -1, -1, 0, 0], 
    [1,  0, -1, -1, 0, 0], 
    [1,  1,  0, -1, 0, 0], 
    [1,  1,  1,  0, 0, 0], 
    [0,  0,  0,  0, -1, 0],  
    [0,  0,  0,  0, 0, -1]]


beforeSigns = ['сначала']
afterSigns = ['потом']
sameTimeSigns = []

def build_hypothesis(text):
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