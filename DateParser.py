import re


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
    print(months_string)

    full_date_regex = '(?P<LongDate>(?P<Day>\\d+)[\\s  ]+(?P<Month>' + \
                      months_string + \
                      ')[\\s  ]+(?P<Year>\\d{4}))'
    print(re.findall(full_date_regex, text))

def find_dot_dates(text):
    dot_date_regex = '(0?[1-9][0-9]).(1?:01|02|03|04|05|06|07|08|09|10|11|12).([1,2][0-9]{3})'

    print(re.findall(dot_date_regex, text))
