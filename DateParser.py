import re

month_days = {
    'января': 0,
    '01': 0,
    '1': 0,
    'февраля': 31,
    '02': 31,
    '2': 31,
    'марта': 59,
    '03': 59,
    '3': 59,
    'апреля': 89,
    '04': 89,
    '4': 89,
    'мая': 119,
    '05': 119,
    '5': 119,
    'июня': 150,
    '06': 150,
    '6': 150,
    'июля': 181,
    '07': 181,
    '7': 181,
    'августа': 212,
    '08': 212,
    '8': 212,
    'сентября': 242,
    '09': 242,
    '9': 242,
    'октября': 273,
    '10': 273,
    'ноября': 304,
    '11': 304,
    'декабря': 334,
    '12': 334,
}


def find_full_dates(text):
    months = ['января', 'февраля', 'марта',
              'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября',
              'октября', 'ноября', 'декабря']

    months_string = ''
    for month in months:
        months_string += '{}|'.format(month)

    for i in range(1, 13):
        months_string += '{}|'.format(i)

    for i in range(1, 10):
        months_string += '0{}|'.format(i)

    months_string = months_string[:-1]

    full_date_regex = '(?P<LongDate>(?P<Day>\\d+)[\\s  ]+(?P<Month>' + \
                      months_string + \
                      ')[\\s  ]+(?P<Year>\\d{4}))'

    print(re.findall(full_date_regex, text))
    return re.findall(full_date_regex, text)


def find_dot_dates(text):
    dot_date_regex = '(0?[1-9][0-9]).(1?:01|02|03|04|05|06|07|08|09|10|11|12).([1,2][0-9]{3})'

    print(re.findall(dot_date_regex, text))
    return re.findall(dot_date_regex, text)


def full_date_to_days(full_date):
    days = 0

    days += int(full_date[1])

    days += int(month_days[full_date[2]])

    year = int(full_date[3])

    days += year * 365 + year % 4 - year / 200

    return days


def dot_date_to_days(dot_date):
    days = 0

    days += int(dot_date[0])

    days += int(month_days[dot_date[1]])

    year = int(dot_date[2])

    days += year * 365 + year % 4 - year / 200

    return days