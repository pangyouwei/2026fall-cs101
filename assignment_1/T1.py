a = int(input())


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return "N"
        else:
            return "Y"
    else:
        return "N"


print(is_leap_year(a))
