import subprocess
import xml.etree.ElementTree as ET
from MulPredicate import MulPredicate


def processText(sentence):
    """
    Обрабатывает текст программой LogicText и возвращает список многоместных предикатов.
    :param sentence: текст для обработки прогаммой LogicText
    :return: список полученных двухместных предикатов
    """
    print ('processing...')

    p = subprocess.Popen('java -jar LogicText8.jar config.properties.nix \"(%s)\"' % sentence, shell=True).wait()
    print ('text processed...')
    print ('parsing...')
    predicates = []
    tree = ET.parse('out.txt')
    root = tree.getroot()
    for predicate in root.findall('.//ru.nsu.fit.makhasoeva.diploma.model.impl.PredicateStatement'):

        predicateName = predicate.find('predicateName').text

        roles = {}
        for element in predicate.findall('./roleToTerm/com.google.common.collect.ImmutableList_-SerializedForm/default/elements/ru.nsu.fit.makhasoeva.diploma.model.impl.PredicateStatement_-Argument'):
            roleName = element.find('roleName').text
            const = element.find('./term/name').text
            roles[roleName] = const    
        predicates.append(MulPredicate(predicateName, roles))
        
    print ('parsed')
    # for index, predicate in enumerate(predicates):
            # predicate.to_special_form().assign_constant_situation(index).to_two_positional()
    return predicates