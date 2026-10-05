str_1 = input().lower().split()
str_2 = input().lower().split()


def compare(a, b):
    return (a > b) - (a < b)


print(compare(str_1, str_2))
