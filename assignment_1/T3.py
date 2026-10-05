M, N = map(int, input().split())


def max_dominoes(a, b):
    area = a * b
    if area % 2 == 0:
        return int(area / 2)
    else:
        return int((area - 1) / 2)


print(max_dominoes(M, N))
