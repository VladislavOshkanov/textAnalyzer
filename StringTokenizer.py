import re
from constants import (
    UNDECIDED,
    SHOULD_SPLIT,
    SHOULD_NOT_SPLIT
)
from regular_expressions import (
    no_punctuation,
    numerical_expression,
    repeated_dash_converter,
    dash_converter,
    right_single_quote_converter,
    simple_dash_finder,
    advanced_dash_finder,
    url_file_finder,
    shifted_ellipses,
    shifted_standard_punctuation,
    multi_single_quote_finder
)



def split_with_locations(text, locations):
    """
     Используем список целых чисел, чтобы разбить строку
     содержащуюся в `text`.
    """
    start = 0
    for pos, type in enumerate(locations):
        if type == SHOULD_SPLIT:
            if start != pos:
                yield text[start:pos]
            start = pos
    if start != len(text):
        yield text[start:]


def mark_regex(regex, text, split_indexes):
    """
    Регулярное выражение, которое добавляет маркер 'SHOULD_SPLIT' в конце
    каждой соответствующей группы данного регулярного выражения.
    """
    for match in regex.finditer(text):
        end_index = match.end()
        if end_index < len(split_indexes):
            split_indexes[end_index] = SHOULD_SPLIT


def mark_begin_end_regex(regex, text, split_indexes):
    """
    Регулярное выражение, которое добавляет маркер 'SHOULD_SPLIT' в конце
    расположение каждой подходящей группы заданного регулярного выражения,
    и добавляет 'SHOULD_SPLIT' в начале
    подходящая группа. Каждый символ в соответствии
    группа будет помечена как 'SHOULD_NOT_SPLIT'.
    """
    for match in regex.finditer(text):
        end_index = match.end()
        begin_index = match.start()

        for i in range(begin_index+1, end_index):
            split_indexes[i] = SHOULD_NOT_SPLIT
        if end_index < len(split_indexes):
            if split_indexes[end_index] == UNDECIDED:
                split_indexes[end_index] = SHOULD_SPLIT
        if split_indexes[begin_index] == UNDECIDED:
            split_indexes[begin_index] = SHOULD_SPLIT


def tokenize(text, normalize_ascii=True):
    """
    Преобразует одну строку в список подстрок
    разделяет пунктуацию и границы слов. Оставляет
    пробелы нетронутыми, всегда прикрепляя их к
    предыдущему токену.
    """
    if no_punctuation.match(text):
        return [text]

    if normalize_ascii:
        text = repeated_dash_converter.sub("-", text)


    split_indexes = [UNDECIDED] * len(text)

    begin_end_regexes = (
        multi_single_quote_finder,
        right_single_quote_converter,
        simple_dash_finder if normalize_ascii else advanced_dash_finder,
        numerical_expression,
        url_file_finder,
        shifted_ellipses,
        shifted_standard_punctuation
    )

    for regex in begin_end_regexes:
        mark_begin_end_regex(regex, text, split_indexes)


    if normalize_ascii:
        text = dash_converter.sub("-", text)
    return list(split_with_locations(text, split_indexes))
