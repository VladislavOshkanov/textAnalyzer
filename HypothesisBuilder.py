from IdChecker import checkForId
from IncludeChecker import checkForInclude

def build_hypothesis_by_predicates(predicates, hypothesis):
    for index1, predicate1 in enumerate(predicates):
                for index2, predicate2 in enumerate(predicates):
                    h = checkForId(predicate1, predicate2, index1, index2)
                    if h and index1 > index2: 
                        print(h.to_string())
                        hypothesis.append(h)

    for index1, predicate1 in enumerate(predicates):
        for index2, predicate2 in enumerate(predicates):
            h = checkForInclude(predicate1, predicate2, index1, index2)
            if h and index1 != index2: 
                print(h.to_string())
                hypothesis.append(h)