a = int(input())


def min_animals(feet):
    if feet % 2 != 0:
        return 0
    else:
        if feet % 4 == 0:
            return int(feet / 4)
        else:
            return int((feet - 2) / 4 + 1)


def max_animals(feet):
    if feet % 2 != 0:
        return 0
    else:
        return int(feet / 2)


print(min_animals(a), max_animals(a))
