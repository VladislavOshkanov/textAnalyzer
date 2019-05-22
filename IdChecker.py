from Hypothesis import Hypothesis


def checkForId(pred1, pred2, cs1, cs2):
    tp_array_1 = pred1.to_special_form().assign_constant_situation(cs1).to_two_positional().two_pos_predicates
    tp_array_2 = pred2.to_special_form().assign_constant_situation(cs1).to_two_positional().two_pos_predicates

    for pred1 in tp_array_1:
        for pred2 in tp_array_2:
            if (pred1.name == pred2.name and (pred1.value[:3] not in pred2.value or pred2.value[:3] not in pred1.value)):
                return None

    return Hypothesis('Id', cs1, cs2)
                   