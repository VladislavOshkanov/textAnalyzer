from LogicText import processText
from Hypothesis import Hypothesis

def process(text):
    return processText(text)



beforeSigns = ['сначала']
afterSigns = ['потом']
sameTimeSigns = []

def build_hypothesis(text):
    hypothesis = []
    beforeSignIndex = -1
    afterSignIndex = -1

    for sign in beforeSigns:
        if (text.find(sign) >= 0):
            beforeSignIndex = text.index(sign)
    for sign in afterSigns:
        if (text.find(sign) >= 0):
            afterSignIndex = text.index(sign)
    
    if (beforeSignIndex < afterSignIndex):
        hypothesis.append(Hypothesis('Before', 1, 2))
    elif (beforeSignIndex > afterSignIndex):
        hypothesis.append(Hypothesis('Before', 2, 1))
    return hypothesis