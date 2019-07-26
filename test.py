from TimeParser import \
    parse_colon_separated_time_without_seconds, \
    parse_colon_separated_time_with_seconds, \
    colon_separated_time_to_seconds
from DateParser import \
    find_full_dates, \
    find_dot_dates, \
    full_date_to_days, \
    dot_date_to_days

find_full_dates("1 мая 2015 2 июня 2020 28.07.1995")

find_dot_dates("28.07.1995")

print(full_date_to_days(find_full_dates("1 мая 2015 2 июня 2020 28.07.1995")[0]))

print(dot_date_to_days(find_dot_dates("28.07.1995")[0]))

print(parse_colon_separated_time_without_seconds("в 18:03 я приеду домой"))

print(parse_colon_separated_time_with_seconds("в 18:03:07 я приеду домой"))

times = parse_colon_separated_time_without_seconds("в 18:03 я приеду домой")

print(colon_separated_time_to_seconds(times[0]))

times = parse_colon_separated_time_with_seconds("в 18:03:07 я приеду домой")

print(colon_separated_time_to_seconds(times[0]))
# process("В комнате сидит маленький мальчик, читающий книгу.")