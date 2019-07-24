from Processor import process
from DateParser import find_full_dates, find_dot_dates, full_date_to_days, dot_date_to_days

find_full_dates("1 мая 2015 2 июня 2020 28.07.1995")

find_dot_dates("28.07.1995")

print(full_date_to_days(find_full_dates("1 мая 2015 2 июня 2020 28.07.1995")[0]))

print(dot_date_to_days(find_dot_dates("28.07.1995")[0]))
# process("В комнате сидит маленький мальчик, читающий книгу.")