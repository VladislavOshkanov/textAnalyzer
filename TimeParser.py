import re


def parse_colon_separated_time_without_seconds(text):
    """
    Находит в тексте время в формате hh:mm
    :param text: исходный текст
    :return:
    """
    regex = '([0-9]?[0-9]):([0-9][0-9])'

    print(re.findall(regex, text))

    return re.findall(regex, text)


def parse_colon_separated_time_with_seconds(text):
    """
    Находит в тексте время в формате hh:mm:ss
    :param text: исходный текст
    :return:
    """
    regex = '([0-9]?[0-9]):([0-9][0-9]):([0-9][0-9])'

    print(re.findall(regex, text))

    return re.findall(regex, text)


def colon_separated_time_to_seconds(time):
    """
    Переводит распарсенное из форматов hh:mm и hh:mm:ss время в секунды
    с начала суток
    :param time:
    :return:
    """
    seconds = 0
    if len(time) == 3:
        seconds = seconds + int(time[0]) * 3600
        seconds = seconds + int(time[1]) * 60
        seconds = seconds + int(time[2])
    elif len(time) == 2:
        seconds = seconds + int(time[0]) * 3600
        seconds = seconds + int(time[1]) * 60

    return seconds
