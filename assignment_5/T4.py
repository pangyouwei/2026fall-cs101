T = int(input())


def sieve(num):
    """返回 num 以下所有质数组成的列表"""

    prime_flags = [True] * (num + 1)
    prime_flags[0], prime_flags[1] = False, False

    for i in range(2, int(num ** 0.5) + 1):
        if prime_flags[i]:
            for j in range(i * i, num + 1, i):
                prime_flags[j] = False

    return [x for x in range(2, num + 1) if prime_flags[x]]


LIMIT = 10 ** 6
primes = set(sieve(LIMIT))

for _ in range(T):
    n = int(input())
    half = n // 2
    i = 0
    while half + i not in primes or half - i not in primes:
        i += 1

    print(half - i, half + i)
